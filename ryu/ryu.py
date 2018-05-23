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
    def __init__(self, *args, **kwargs):
        super(RyuFurioso, self).__init__(*args, **kwargs)

    