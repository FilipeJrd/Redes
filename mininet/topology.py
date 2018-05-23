
from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        s1 = self.addSwitch('s1', protocols='OpenFlow10')
        s2 = self.addSwitch('s2', protocols='OpenFlow10')
        s3 = self.addSwitch('s3', protocols='OpenFlow10')

        
        client1 = self.addHost('client1', ip='1.1.1.3/30',defaultRoute=None )
        client2 = self.addHost('client2', ip='2.2.2.3/30',defaultRoute=None )
        client3 = self.addHost('client3', ip='3.3.3.3/30',defaultRoute=None )

        
        server1 = self.addHost('server1', ip='1.1.1.2/30',defaultRoute=None )
        server2 = self.addHost('server2', ip='2.2.2.2/30',defaultRoute=None )
        server3 = self.addHost('server3', ip='3.3.3.2/30',defaultRoute=None )
        # Add links
        self.addLink( client1, s1 )
        self.addLink( server1, s1 )

        self.addLink( client2, s2 )
        self.addLink( server2, s2 )

        self.addLink( client3, s3 )
        self.addLink( server3, s3 )

        
        self.addLink( s1, s2 )
        self.addLink( s2, s3 )
        self.addLink( s3, s1 )

topos = { 'mytopo': ( lambda: MyTopo() ) }
