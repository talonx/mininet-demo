from mininet.topo import Topo, LinearTopo;
from mininet.net import Mininet;
from mininet.cli import CLI;

class Basic(Topo):

    def __init__(self):
        Topo.__init__(self)

        h1 = self.addHost("h1");
        h2 = self.addHost("h2");

        s1 = self.addSwitch("s1");

        self.addLink(h1, s1, bw=1, delay="10ms", loss=0, max_queue_size=1000, use_htb=True);
        self.addLink(h2, s1, bw=1, delay="10ms", loss=0, max_queue_size=1000, use_htb=True);

topo = Basic();
net = Mininet(topo=topo) # Uses the default reference controller
net.start()

h1 = net.get("h1");
res = h1.cmd("route -n")
print(res)

net.stop()
