from numpy import *
from multiprocessing import Pool,current_process
from collections import deque
import time
import __builtin__ as std

d = 3
Beta = arange(0.1,0.3,0.005)

def nbr (x,todo,nbrdelta) :
    #for i in range(d) : 
    #    todo.append((x+ n**i)%grootte)
    #    todo.append((x- n**i)%grootte)
    todo.extend([(x+i)%grootte for i in nbrdelta])

def hexnbr (x,todo) :
    for i in range(d) : 
        todo.append((x+ n**i)%grootte)
        todo.append((x- n**i)%grootte)
    todo.append((x+ n-1)%grootte)
    todo.append((x- n+1)%grootte)


def run (beta) :
    t = time.clock()
    #Total magnetization
    M = zeros(steps)
    random.seed()
    p = current_process()
    spins = random.randint(0,2,grootte)
    M[0] = 2.0*sum(spins)-grootte
    randloc = random.randint(0,grootte,steps)
    nbrdelta =[]
    for i in range(d) :
        nbrdelta += [n**i,-n**i]
    Padd = 1-exp(-2*beta)
    for i in range(steps-1) :
        x = randloc[i]
        xspin = spins[x]
        spins[x] = 1-spins[x]
        cluster = 1
        todo = deque()
        nbr(x,todo,nbrdelta)
        while todo :
            y = todo.pop()
            if spins[y] == xspin and Padd > random.random() :
                nbr(y,todo,nbrdelta)
                spins[y] = 1-spins[y]
                cluster += 1
        M[i+1] = M[i] + cluster*2*(2*spins[x]-1)
    t = time.clock() - t
    print 'beta =', beta, ', n =', n , 'data generated in', t, 'at', p.name
    M = array(M[steps/3:steps])
    #Chi = susceptibility per spin
    Chi = beta*(mean(M**2,0)-mean(absolute(M),0)**2)/grootte
    #Mabs absolute value of the mean magnetization per spin
    Mabs = mean(absolute(M),0)/grootte
    return (Chi,Mabs,t)
  

name = '3Dwolfftest'
if __name__ == '__main__':
    for n in [20] :
        steps = 15000
        Chi = []
        Mabs = []
        t = []
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
