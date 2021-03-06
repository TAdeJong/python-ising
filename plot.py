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
Mabs = load(name+'_'+'Mabs'+'.npy')
#E = load(name+'_'+'E'+'.npy')
beta = load(name+'_'+'beta'+'.npy')
Chi = load(name+'_'+'Chi'+'.npy')
plot.figure(0)
plot.plot(beta,Chi)
plot.ylabel(r'$\chi$')
plot.xlabel(r'$\beta J$')
plot.title(r'$\chi$ as a function of $\beta J$')
plot.legend(loc=0)
plot.figure(1)
plot.plot(beta,Mabs)
plot.legend()
plot.ylabel(r'$|m|$')
plot.xlabel(r'$\beta J$')
plot.title(r'$|m|$ as a function of $\beta J$')
plot.ioff()
plot.show()
