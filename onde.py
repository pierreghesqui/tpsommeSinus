import numpy as np
class Onde :
    def __init__(self,f,retard=0):
        self.frequence = f
        self.retard = retard
        self.fe = 44100
        self.duree  = 1
        self.signal = self.sinu()
        
    def sinu(self):
        t1 = np.arange(0,self.duree,1/self.fe) 
        y1 = np.sin(2 * np.pi* self.frequence * (t1+self.retard))
        self.temps = t1
        return y1
    
    def __add__(self, other):
        onde2 = Onde(self.frequence)
        onde2.signal = self.signal + other.signal
        return onde2

