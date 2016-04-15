#vim : tabstop=8 expandtab shiftwidth=4 softtabstop=4
from numpy import *
import matplotlib.pyplot as plot
from multiprocessing import Pool,current_process
import time
import __builtin__ as std

d = 2
n = 40
Beta = arange(0.3,0.5,0.02)
grootte = n**d
steps = 300*grootte

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
    spins = random.randint(0,2,grootte)
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
    return (M,E)


M = []
E = []
Cm = []
Ce = []
name = 'thermrand'
iters = 50
p = Pool()
for i in range(len(Beta)) :
    if __name__ == '__main__':
        args = [(grootte, steps, Beta[i])]*iters
        Mtemp = zeros(steps)
        Etemp = zeros(steps)
        for res in p.map(run, args):
            Mtemp+=absolute(res[0])
            Etemp+=absolute(res[1])
        E.append(list(Etemp/double(iters)))
        M.append(list(Mtemp/double(iters)))
print('Done simulating, saving data...')
save(name+'E',E)
save(name+'M',M)

