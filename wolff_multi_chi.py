from numpy import *
from multiprocessing import Pool,current_process
from collections import deque
import time
import __builtin__ as std

d = 2
Beta = arange(0.42,0.44,0.0005)

def nbr (x,todo) :
    for i in range(d) : 
        todo.append((x+ n**i)%grootte)
        todo.append((x- n**i)%grootte)

def hexnbr (x,todo) :
    for i in range(d) : 
        todo.append((x+ n**i)%grootte)
        todo.append((x- n**i)%grootte)
    todo.append((x+ n-1)%grootte)
    todo.append((x- n+1)%grootte)


def run (beta) :
    t = time.clock()
    M = zeros(steps)
    random.seed()
    p = current_process()
    spins = random.randint(0,2,grootte)
    M[0] = 2.0*sum(spins)-grootte
    randloc = random.randint(0,grootte,steps)
    Padd = 1-exp(-2*beta)
    for i in range(steps-1) :
        x = randloc[i]
        xspin = spins[x]
        spins[x] = 1-spins[x]
        cluster = 1
        todo = deque()
        nbr(x,todo)
        while todo :
            y = todo.pop()
            if spins[y] == xspin and Padd > random.random() :
                nbr(y,todo)
                spins[y] = 1-spins[y]
                cluster += 1
        M[i+1]=M[i] + cluster*2*(2*spins[x]-1)
    t = time.clock() - t
    print 'beta =', beta, ', n =', n , 'data generated in', t, 'at', p.name
    M = array(M[grootte:steps])
    Chi = beta*(mean(M**2,0)-mean(absolute(M),0)**2)/grootte
    Mabs = mean(absolute(M),0)/grootte
    return (Chi,Mabs,t)
name = 'wolffzoom'
if __name__ == '__main__':
    for n in [100] :
        Chi = []
        Mabs = []
        t = []
        steps = 12000
        grootte = n**d
        p = Pool()
        #args = map(lambda b: (grootte, steps, b), beta)
        save(name+'_'+str(n)+'_beta', Beta)
        for res in p.map(run, Beta):
            Chi.append(res[0])
            Mabs.append(res[1])
            t.append(res[2])
        print('Done simulating for n = '+str(n)+', saving data')
        save(name+'_'+str(n)+'_Chi', Chi)
        save(name+'_'+str(n)+'_Mabs', Mabs)
        save(name+'_'+str(n)+'_time', t)
