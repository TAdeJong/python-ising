import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import sys

n=[10,20,30]
name = sys.argv[1]
print name
if len(sys.argv) > 2 :
    n = sys.argv[2]

fig, (axchi, axbeta) = plt.subplots(1,2)
plt.subplots_adjust(bottom=0.30)
gamma0 = 7./4.
nu0 = 1.0
betac0 = 1/2.6
expbeta0 = 0.125
plots = []
bplots =[]
beta = []
Chi = []
Mabs = []
for i, L in enumerate(n) :
    Chi.append(np.load(name+'_'+str(L)+'_Chi'+'.npy'))
    beta.append(np.load(name+'_'+str(L)+'_beta'+'.npy'))
    Chiprime = L**(-gamma0/nu0)*Chi[i]
    x = L**(1/nu0)*(betac0/beta[i]-1)
    l, = axchi.plot(x,Chiprime,label='n = '+str(L))
    plots.append(l)
axchi.set_ylabel(r'$\chi$')
axchi.set_xlabel(r'$\beta J$')
axchi.set_title(r'Scaled Susceptibility as a function of critical temperature')
plt.legend(loc=0)

for i, L in enumerate(n) :
   Mabs.append(np.load(name+'_'+str(L)+'_Mabs'+'.npy'))
   Mabsprime = L**(expbeta0/nu0)*Mabs[i]
   x = L**(1/nu0)*(betac0/beta[i]-1)
   l, = axbeta.plot(x,Mabsprime,label='n = '+str(L))
   bplots.append(l)
axbeta.legend(loc=1)
axbeta.set_ylabel(r'$|m|$')
axbeta.set_xlabel(r't')
axbeta.set_title(r'Mean magnetisation $|m|$ as a function of critical temperature')

axcolor = 'lightgoldenrodyellow'
axgamma = plt.axes([0.1, 0.1, 0.65, 0.03], axisbg=axcolor)
axnu = plt.axes([0.1, 0.14, 0.65, 0.03], axisbg=axcolor)
axTc = plt.axes([0.1, 0.22, 0.65, 0.03], axisbg=axcolor)
axexpbeta = plt.axes([0.1, 0.18, 0.65, 0.03], axisbg=axcolor)

sgamma = Slider(axgamma, 'Gamma', 0.5, 2.0, valinit=gamma0, valfmt='%0.4f')
snu = Slider(axnu, 'Nu', 0.2, 2.0, valinit=nu0, valfmt='%0.4f')
sTc = Slider(axTc, 'Tc', 5.0, 15.0, valinit=1/betac0, valfmt='%0.4f')
sexpbeta = Slider(axexpbeta, 'Beta', -0.6, 0.6, valinit=expbeta0, valfmt='%0.4f')



def update(val):
    gamma = sgamma.val
    nu = snu.val
    betac = 1.0/sTc.val
    expbeta = sexpbeta.val
    for i, L in enumerate(n) :
        Chiprime = L**(-gamma/nu)*Chi[i]
        x = L**(1/nu)*(betac/beta[i]-1)
        plots[i].set_ydata(Chiprime)
        plots[i].set_xdata(x)
        Mabsprime = L**(expbeta/nu)*Mabs[i]
        bplots[i].set_ydata(Mabsprime)
        bplots[i].set_xdata(x)
    axchi.relim()
    axchi.autoscale_view(True,True,True)
    axbeta.relim()
    axbeta.autoscale_view(True,True,True)
    fig.canvas.draw()

sgamma.on_changed(update)
snu.on_changed(update)
sTc.on_changed(update)
sexpbeta.on_changed(update)

plt.show()


