#vim : tabstop=8 expandtab shiftwidth=4 softtabstop=4
from numpy import *
import matplotlib.pyplot as plot
from multiprocessing import Pool,current_process
import time
import __builtin__ as std

d = 2
n = 40
Beta = arange(0.3,0.5,0.05)
grootte = n**d
steps = 500*grootte
correl = True

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
    E = zeros(steps)
    M = zeros(steps)
    random.seed()
    p = current_process()
    spins = random.randint(0,1,grootte)
    E[0] = Etot(spins)
    M[0] = 2.0*sum(spins)-grootte
    randloc = random.randint(0,grootte,steps)
    randP = random.random(steps)
    for i in range(steps-1) :
        x = randloc[i]
        dE = H(spins,x)
        if(min(exp(dE*beta),1) > randP[i]) :
            spins[x]=1-spins[x]
            E[i+1] = E[i]+dE
            M[i+1] = M[i]+2*(2*spins[x]-1)
        else :
            M[i+1] = M[i]
            E[i+1] = E[i]
    t = time.clock() - t
    print 'beta =', beta, ', n =', n , 'data generated in', t, 'at', p.name
    M = M[(100*grootte):steps]
    E = E[(100*grootte):steps]
    Chi = beta*(mean(M**2,0)-mean(absolute(M),0)**2)/grootte
    Mabs = mean(absolute(M),0)/grootte
    return (E,Mabs,Chi,t)

def correlrun ((grootte, steps, beta)) :
    t = time.clock()
    E = zeros(steps)
    M = zeros(steps)
    random.seed()
    p = current_process()
    spins = random.randint(0,1,grootte)
    E[0] = Etot(spins)
    M[0] = 2.0*sum(spins)-grootte
    randloc = random.randint(0,grootte,steps)
    randP = random.random(steps)
    for i in range(steps-1) :
        x = randloc[i]
        dE = H(spins,x)
        if(min(exp(dE*beta),1) > randP[i]) :
            spins[x]=1-spins[x]
            E[i+1] = E[i]+dE
            M[i+1] = M[i]+2*(2*spins[x]-1)
        else :
            M[i+1] = M[i]
            E[i+1] = E[i]
    t = time.clock() - t
    print 'beta =', beta, ', n =', n , 'data generated in', t, 'at', p.name
    M = M[(100*grootte):steps]
    E = E[(100*grootte):steps]
    E -= mean(E)
    M = absolute(M)
    Mabs = mean(M,0)/grootte
    M -= mean(M)
    Cm = correlate(M,M, mode='same')
    Cm /=max(Cm)
    Ce = correlate(E,E, mode='same')
    Ce /=max(Ce)
    print 'beta =', beta, ', n =', n , 'data correlated in', t, 'at', p.name
    return (E, Mabs, Cm, Ce)


Chi = []
Mabs = []
simtime = []
E = []
Cm = []
Ce = []
name = 'metronorm'
if __name__ == '__main__':
    args = map(lambda b: (grootte, steps, b), Beta)
    p = Pool()
    if correl :
        for res in p.map(correlrun, args):
            E.append(res[0])
            Mabs.append(res[1])
            Cm.append(res[2])
            Ce.append(res[3])
    else :
        for res in p.map(run, args):
            E.append(res[0])
            Mabs.append(res[1])
            Chi.append(res[2])
            simtime.append(res[3])
print('Done simulating, saving data...')
save(name+'_beta', Beta)
save(name+'_Mabs', Mabs)
save(name+'_E', E)
if correl :
    save(name+'_Cm', Cm)
    save(name+'_Ce', Ce)
else :
    save(name+'_Chi', Chi)
    save(name+'_time', simtime)

