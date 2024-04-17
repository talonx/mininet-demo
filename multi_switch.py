from mininet.topo import Topo, LinearTopo;
from mininet.net import Mininet;
from mininet.cli import CLI;

class Lan(Topo):

    def __init__(self):
        Topo.__init__(self)

        s1 = self.addSwitch("s1");
        s2 = self.addSwitch("s2");
        h1 = self.addHost("h1");
        h2 = self.addHost("h2");
        
        # Link host 1 to switch 1
        self.addLink(h1, s1, bw=1, delay="10ms", loss=0, max_queue_size=1000, use_htb=True);
        # Link host 2 to switch 2
        self.addLink(h2, s2, bw=1, delay="10ms", loss=0, max_queue_size=1000, use_htb=True);
        # Link switch 1 to switch 2
        self.addLink(s1, s2, bw=1, delay="10ms", loss=0, max_queue_size=1000, use_htb=True);

topo = Lan();
net = Mininet(topo=topo) # Uses the default reference controller
net.start()
CLI(net)
net.stop()
