
from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        
        client1 = self.addHost('client1')
        client2 = self.addHost('client2')
        client3 = self.addHost('client3')

        
        server1 = self.addHost('server1')
        server2 = self.addHost('server2')
        server3 = self.addHost('server3')
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
