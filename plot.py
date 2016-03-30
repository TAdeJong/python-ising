from numpy import *
import matplotlib.pyplot as plot
import __builtin__ as std
import sys



n = 40
name = sys.argv[1]
print name
if len(sys.argv) > 2 :
	n = sys.argv[2]
d = 2
steps = 20*n**d
grootte = n**d
beta = load(name+'_'+'beta'+'.npy')
Chi = load(name+'_'+'Chi'+'.npy')
Mabs = load(name+'_'+'Mabs'+'.npy')
plot.figure(0)
plot.plot(beta,Chi,label='Chi')
plot.ylabel(r'$\chi$')
plot.xlabel(r'$\beta$')
plot.legend(loc=0)
plot.figure(1)
plot.plot(beta,Mabs)
plot.legend()
plot.ylabel(r'$|m|$')
plot.xlabel(r'$\beta$')
#plot.ylabel('Chi')
#plot.xlabel('beta')
plot.ioff()
plot.show()
