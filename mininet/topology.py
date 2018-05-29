from mininet.node import CPULimitedHost
from mininet.topo import Topo
from mininet.link import Link
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.util import custom
from mininet.link import TCIntf

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        s1 = self.addSwitch('s1', protocols='OpenFlow13', dpid="0000000000000001", mac= '01:00:00:00:00:00')
        s2 = self.addSwitch('s2', protocols='OpenFlow13', dpid="0000000000000002", mac= '02:00:00:00:00:00')
        s3 = self.addSwitch('s3', protocols='OpenFlow13', dpid="0000000000000003", mac= '03:00:00:00:00:00')

        
        client1 = self.addHost('client1', mac= '00:00:00:00:01:01')
        client2 = self.addHost('client2', mac= '00:00:00:00:01:02')
        client3 = self.addHost('client3', mac= '00:00:00:00:01:03')

        
        server1 = self.addHost('server1', mac= '00:00:00:00:02:01')
        server2 = self.addHost('server2', mac= '00:00:00:00:02:02')
        server3 = self.addHost('server3', mac= '00:00:00:00:02:03')
        # Add links
        # 30Kbytes = 0.24 Mbits
        self.addLink( client1, s1, port2=1 )
        self.addLink( server1, s1, port2=2 )

        self.addLink( client2, s2, port2=1 )
        self.addLink( server2, s2, port2=2 )

        self.addLink( client3, s3, port2=1 )
        self.addLink( server3, s3, port2=2 )

        
        self.addLink( s1, s2, port1=3, port2=4)
        self.addLink( s2, s3, port1=3, port2=4 )
        #self.addLink( s3, s1, port1=3, port2=4 )


def run():
    c = RemoteController('c', '0.0.0.0', 6633)
    intf = custom(TCIntf, bw=0.24)
    net = Mininet(topo=MyTopo(), intf=intf, host=CPULimitedHost, controller=None)
    net.addController(c)
    net.start()

    # installStaticFlows( net )
    CLI(net)
    net.stop()

# if the script is run directly (sudo custom/optical.py):
if __name__ == '__main__':
    setLogLevel('info')
    run()