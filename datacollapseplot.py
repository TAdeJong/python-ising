from numpy import *
import matplotlib.pyplot as plot
import __builtin__ as std
import sys


n=[20,30,40,50,60]
name = sys.argv[1]
print name
if len(sys.argv) > 2 :
    n = sys.argv[2]
d = 2
#steps = 20*n**d
#grootte = n**d
#E = load(name+'_'+'E'+'.npy')
gamma = 1.76
nu = 1.00
betac = 1/2.269
beta = load(name+'_40_beta'+'.npy')
expbeta = 1./8.
plot.figure(0)
for L in n :
    Chi = load(name+'_'+str(L)+'_Chi'+'.npy')
    Chi = L**(-gamma/nu)*Chi
    x = L**(1/nu)*(betac/beta-1)
    plot.plot(x,Chi,label='n = '+str(L))
plot.ylabel(r'$\chi$')
plot.xlabel(r'$\beta J$')
plot.title(r'Scaled Susceptibility as a function of critical temperature')
plot.legend(loc=0)
plot.figure(1)
for L in n :
    Mabs = load(name+'_'+str(L)+'_Mabs'+'.npy')
    Mabs = L**(expbeta/nu)*Mabs
    x = L**(1/nu)*(betac/beta-1)
    plot.plot(x,Mabs,label='n = '+str(L))
plot.legend(loc=1)
plot.ylabel(r'$|m|$')
plot.xlabel(r't')
plot.title(r'Mean magnetisation $|m|$ as a function of critical temperature')
plot.ioff()
plot.show()
