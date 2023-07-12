import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio,display

def voirSignaux(ondes):
    nbondes = np.shape(ondes)[0]
    retard =0
    couleurs =["b-","g-","m-"]
    labels = ["onde1 ", "onde2 ", "ondetotale "]
    for i in range(nbondes):
        onde = ondes[i]
        retard = max(retard,onde.retard)
        
    plt.text(5.1/ondes[0].frequence,1,"retard = "+str(round(retard,2))+' s',size=12,
        bbox =dict(boxstyle="round",ec=("k"),fc=("c")))
    for i in range(nbondes):
        plt.plot(ondes[i].temps,ondes[i].signal,couleurs[i], label = labels[i])
    
    plt.legend(loc= 'upper right')
    plt.title("Y = sin(2$\pi$f)")
    plt.xlabel("temps (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.xlim(0,5*1/ondes[0].frequence)
    plt.ylim(-2.2,2.2)
    plt.ticklabel_format(style='scientific',axis='x',scilimits=(0,0))
    plt.show()
    
def entendreLeSon(y):
    '''
    Cette fonction permet d'entendre le son
    Exemple: 
    note1 = note(440,1,1)
    entendreLeSon(note1)
    '''
    y=y.signal
    te = 1/44100
    fe = 1/te
    duration_s = te*(y.shape[0]-1)
    # Play the waveform out the speakers
    y = y/2.001
    if np.max(y)>1:
        display(Audio(y, rate=fe,autoplay=True))
    else:
        display(Audio(y, rate=fe,autoplay=True,normalize=False))
    
    
    return 1
 
