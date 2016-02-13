from numpy import *
import matplotlib.pyplot as plot
from multiprocessing import Pool,current_process
import time
import __builtin__ as std

d = 2
n = 40
steps = 1000*n**d
beta = arange(0.3,0.6,0.01)
grootte = n**d

def H (spins,x) :
    "Returns the energy value in case of a spin flip at location x in spins"
    H = 0
    for i in range(d) :
        H += spins[(x+ n**i)%spins.size]+spins[(x-n**i)%spins.size]-1
    H*= (2**d)*(1-2*spins[x%spins.size])
    return H

def Etot (spins) :
    "Returns the energy in spins"
    dE = 0
    E = 0
    for i in range(d) : 
        for x in spins :
            dE = 2*spins[(x+ n**i)%spins.size]-1 
            dE*= (2*spins[x%spins.size]-1)
            E+=dE;
    return E


def run ((grootte, steps, beta)) :
    t = time.clock()
    M = []
    random.seed()
    p = current_process()
    spins = random.randint(0,1,grootte)
    M.append(2.0*sum(spins)-grootte)
    randloc = random.randint(0,grootte,steps)
    randP = random.random(steps)
    for i in range(steps-1) :
        x = randloc[i]
            dE = H(spins,x)
        if(min(exp(dE*beta),1) > randP[i]) :
            spins[x]=1-spins[x]
            M.append(M[-1]+2*(2*spins[x]-1))
        else :
            M.append(M[-1])
    t = time.clock() - t
    print 'beta =', beta, ', n =', n , 'data generated in', t, 'at', p.name
    M = array(M[(100*grootte):steps])
    Chi = beta*(mean(M**2,0)-mean(absolute(M),0)**2)/grootte
    Mabs = mean(absolute(M),0)/grootte
    return (Chi,Mabs,t)

Chi = []
Mabs = []
if __name__ == '__main__':
    args = map(lambda b: (grootte, steps, b), beta)
    p = Pool()
    for res in p.map(run, args):
        Chi.append(res[0])
        Mabs.append(res[1])
print('Done simulating, starting plotting...')
plot.figure(0)
plot.plot(beta,Chi)
plot.ylabel(r'$\chi$')
plot.xlabel(r'$\beta$')
plot.figure(1)
plot.plot(beta,Mabs)
plot.ylabel(r'$|m|$')
plot.xlabel(r'$\beta$')
plot.show()
