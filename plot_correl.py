#vim : tabstop=8 expandtab shiftwidth=4 softtabstop=4
from numpy import *
import matplotlib.pyplot as plot
import __builtin__ as std
import sys
import time


n = 40
name = sys.argv[1]
print name
if len(sys.argv) > 2 :
	n = sys.argv[2]
d = 2
grootte = n**d
t = time.clock()
beta = load(name+'_'+'beta'+'.npy')
Ce = load(name+'_'+'Ce'+'.npy')
Cm = load(name+'_'+'Cm'+'.npy')
E = load(name+'_'+'E'+'.npy')
t = time.clock() - t
print 'data loaded in', t

mag = Cm
energy = Ce
mag = array(mag)
mag = mag.reshape([size(beta),-1])
mag = mag.transpose()
energy = array(energy)
energy = energy.reshape([size(beta),-1])
energy = energy.transpose()
labels = []
for i in beta :
	labels.append(r'$\beta$J = '+ str(i))

plot.figure(1)
plot.plot(arange(-shape(energy)[0]/(2*grootte),shape(energy)[0]/(2*grootte),1.0/grootte),energy)
plot.ylabel(r'$c_e$')
plot.xlabel(r'$\Delta t$ (steps/spin)')
plot.title('Normalized autocorrelation of the Energy')
plot.legend(labels)
plot.figure(2)
plot.plot(arange(-shape(energy)[0]/(2*grootte),shape(energy)[0]/(2*grootte),1.0/grootte),mag)
plot.ylabel(r'$c_m$')
plot.xlabel(r'$\Delta t$ (steps/spin)')
plot.title('Normalized autocorrelation of the Magnetisation')
plot.legend(labels)
plot.show()
