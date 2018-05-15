
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
        client1.cmd('ifconfig client1-eth0 inet 1.1.1.3/30')

        client2 = self.addHost('client2')
        client2.cmd('ifconfig client2-eth0 inet 2.2.2.3/30')

        client3 = self.addHost('client3')
        client3.cmd('ifconfig client3-eth0 inet 3.3.3.3/30')

        
        server1 = self.addHost('server1')
        client1.cmd('ifconfig client1-eth0 inet 1.1.1.2/30')
        
        server2 = self.addHost('server2')
        server2.cmd('ifconfig server2-eth0 inet 2.2.2.2/30')
        
        server3 = self.addHost('server3')
        server3.cmd('ifconfig server3-eth0 inet 3.3.3.2/30')

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
