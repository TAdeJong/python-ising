#vim : tabstop=8 expandtab shiftwidth=4 softtabstop=4
from numpy import *
import matplotlib.pyplot as plot
from multiprocessing import Pool,current_process
import time
import __builtin__ as std
import sys

d = 2
n = 40
Beta = arange(0.3,0.5,0.02)
grootte = n**d
steps = 300*grootte

name1 = sys.argv[1]
name2 = sys.argv[2]
print name1, name2


M = []
E = []
Cm = []
Ce = []
iters = 50
p = Pool()
E=load(name1+'E.npy')
M=load(name1+'M.npy')
Mdata1 = array(M)
Mdata1 = Mdata1.transpose()
Edata1 = array(E)
Edata1 = Edata1.transpose()
E=load(name2+'E.npy')
M=load(name2+'M.npy')
Mdata2 = array(M)
Mdata2 = Mdata2.transpose()
Edata2 = array(E)
Edata2 = Edata2.transpose()

labels = []
for i in Beta :
	labels.append(r'$\beta$J = '+ str(i))
f, ((ax1,ax2),(ax3,ax4)) = plot.subplots(2,2, sharex='col', sharey='row')
ax1.set_title('Relaxation')
ax1.plot(arange(0,steps/grootte,1.0/grootte),Mdata1)
plot.legend(labels)
plot.xlabel('Metropolis steps per lattice site')
ax1.set_ylabel(r'Magnetization $|m|$')
#plot.figure(1)
ax2.plot(arange(0,steps/grootte,1.0/grootte),Mdata1)
#plot.legend(labels)
#plot.title('Energy Relaxation')
#ax2.ylabel('Metropolis steps per lattice site')
ax3.set_ylabel(r'Magnetic Energy')
ax3.plot(arange(0,steps/grootte,1.0/grootte),Edata1)
ax4.plot(arange(0,steps/grootte,1.0/grootte),Edata2)
ax1.set_ylim([0, 1600])
ax3.set_ylim([0, 3600])
plot.show()
