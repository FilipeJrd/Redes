
from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types


class L2Switch(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(L2Switch, self).__init__(*args, **kwargs)

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        in_port = msg.match['in_port']

        pkt = packet.Packet(msg.data)
        eth = pkt.get_protocols(ethernet.ethernet)[0]

        if eth.ethertype == ether_types.ETH_TYPE_LLDP:
            # ignore lldp packet
            return
        dst = eth.dst
        src = eth.src

        self.logger.info("packet in %s %s %s %s", datapath, src, dst, in_port)

        client_server = (src.startswith('00:00:00:00:01') and dst.startswith('00:00:00:00:02'))
        server_client = (src.startswith('00:00:00:00:02') and dst.startswith('00:00:00:00:01'))

        if not (client_server or server_client):
          self.logger.info("Entrou")
          actions = [parser.OFPActionOutput(ofproto.OFPP_FLOOD)]
          out = parser.OFPPacketOut(
              datapath=datapath, buffer_id=msg.buffer_id, in_port=in_port,
              actions=actions)
          datapath.send_msg(out)
        else:
          self.logger.info("Block")