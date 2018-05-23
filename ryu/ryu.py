import struct

from ryu.base import app_manager
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_0
from ryu.lib import dpid as dpid_lib
from ryu.lib import stplib
from ryu.lib.mac import haddr_to_str
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet

class RyuFurioso(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]
    _CONTEXTS = {'stplib': stplib.Stp}

    def __init__(self, *args, **kwargs):
        super(RyuFurioso, self).__init__(*args, **kwargs)
        self.mac_to_port = {}
        self.stp = kwargs['stplib']

    