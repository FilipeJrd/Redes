
from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.lib import stplib
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types
from ryu.ofproto import ofproto_v1_3


class L2Switch(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]
    _CONTEXTS = {'stplib': stplib.Stp}

    def __init__(self, *args, **kwargs):
        super(L2Switch, self).__init__(*args, **kwargs)
        self.mac_to_port = {} # initializes mac-to-port table
        self.stp = kwargs['stplib'] # set spanning tree field

    @set_ev_cls(stplib.EventPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        msg = ev.msg 
        datapath = msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        in_port = msg.match['in_port']

        pkt = packet.Packet(msg.data)
        eth = pkt.get_protocol(ethernet.ethernet)

        src = eth.src # mac addr of src
        dst = eth.dst # mac addr of dst

        dpid = datapath.id
        self.mac_to_port.setdefault(dpid, {})

        self.logger.info("packet in %s %s %s %s", datapath, src, dst, in_port)

        # update mac-to-port table to avoid another packet flood.
        self.mac_to_port[dpid][src] = in_port

        # perform mac-to-port lookup.
        if dst in self.mac_to_port[dpid]:
            out_port = self.mac_to_port[dpid][dst]
        else:
            out_port = ofproto.OFPP_FLOOD

        # allowed packet flows
        switch1_switch2 = (src.startswith('01') and dst.startswith('02'))
        switch2_switch3 = (src.startswith('02') and dst.startswith('03'))
        switch3_switch1 = (src.startswith('03') and dst.startswith('01'))

        # defines the action (drop packets if src-dst is not authorized).
        actions = [parser.OFPActionOutput(out_port)]
        if not (switch1_switch2 or switch2_switch3 or switch3_switch1):
            print("{} - {} is NOT authorized for communication".format(src, dst))
            actions = []

        # add flow to avoid further triggering of this event.
        if out_port != ofproto.OFPP_FLOOD:
            self.add_flow(datapath, msg.in_port, dst, src, actions)

        out = parser.OFPPacketOut(datapath=datapath, buffer_id=msg.buffer_id,
                                  in_port=in_port, actions=actions)
        datapath.send_msg(out)
    
    def add_flow(self, datapath, in_port, dst, src, actions):
        ofproto = datapath.ofproto

        wildcards = ofproto_v1_3.OFPFW_ALL
        wildcards &= ~ofproto_v1_3.OFPFW_IN_PORT
        wildcards &= ~ofproto_v1_3.OFPFW_DL_DST

        match = datapath.ofproto_parser.OFPMatch(wildcards=wildcards,
                                                 in_port=in_port,
                                                 eth_src=src,
                                                 eth_dst=dst)

        mod = datapath.ofproto_parser.OFPFlowMod(
            datapath=datapath, match=match, cookie=0,
            command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
            priority=ofproto.OFP_DEFAULT_PRIORITY,
            flags=ofproto.OFPFF_SEND_FLOW_REM, actions=actions)
        datapath.send_msg(mod)