from numpy import *
import matplotlib.pyplot as plot
import __builtin__ as std
import sys


n=[20,30]
name = sys.argv[1]
print name
if len(sys.argv) > 2 :
	n = sys.argv[2]
d = 2
#steps = 20*n**d
#grootte = n**d
#E = load(name+'_'+'E'+'.npy')
beta = load(name+'_40_beta'+'.npy')
plot.figure(0)
for i in n :
    Chi = load(name+'_'+str(i)+'_Chi'+'.npy')
    plot.plot(beta,Chi,label='n = '+str(i))
plot.ylabel(r'$\chi$')
plot.xlabel(r'$\beta J$')
plot.title(r'Susceptibility as a function of inverse temperature')
plot.legend(loc=0)
plot.figure(1)
for i in n :
    Mabs = load(name+'_'+str(i)+'_Mabs'+'.npy')
    plot.plot(beta,Mabs,label='n = '+str(i))
plot.legend(loc=2)
plot.ylabel(r'$|m|$')
plot.xlabel(r'$\beta J$')
plot.title(r'Mean magnetisation $|m|$ as a function of inverse temperature')
plot.ioff()
plot.show()
