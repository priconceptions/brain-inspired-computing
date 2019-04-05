# implementation of the Hodgkin-Huxley model based on http://www.tqmp.org/RegularArticles/vol13-2/p105/p105.pdf
import numpy as np
import matplotlib.pyplot as plt
from math import exp, expm1

class HH:
    def __init__(self, I=1.5):
        self.I = I

        # all neuron properties
        self.totalTime = 50
        self.deltaT = 0.001
        self.time = np.arange(0, self.totalTime, self.deltaT)
        self.V = np.zeros(len(self.time))
        self.n = np.zeros(len(self.time))
        self.n[0] = 0
        self.m = np.zeros(len(self.time))
        self.m[0] = 0
        self.h = np.zeros(len(self.time))
        self.h[0] = 1
        self.g_Na = 120
        self.g_K = 36
        self.g_L = 0.3
        self.V_Na = 115
        self.V_K = -12
        self.V_L = 10.6
        self.C = 1

    def alpha_n(self, V):
        return (0.1-0.01*(V+65)) / (np.exp(1-0.1*(V+65)) - 1)
    def beta_n(self, V):
        return 0.125*np.exp(-(V+65)/80)
    def alpha_m(self, V):
        return (2.5 - 0.1*(V+65)) / (np.exp(2.5-0.1*(V+65)) - 1)
    def beta_m(self, V):
        return 4*np.exp(-(V+65)/18)
    def alpha_h(self, V):
        return 0.07*np.exp(-(V+65)/20)
    def beta_h(self, V):
        return 1/(np.exp(3.0-0.1*(V+65)) + 1)

    def NaPart(self, m, h, V):
        return self.g_Na * (m**3) * h * (self.V_Na - (V+65))
    
    def KPart(self, n, V):
        return self.g_K * (n**4) * (self.V_K - (V+65))
    
    def ClPart(self, V):
        return self.g_L * (self.V_L - (V+65))
    
    def plotNeuronActivity(self):
        self.V[0] = -55
        for i in range(1, len(self.time)):

            self.V[i] = self.V[i-1] + self.deltaT * ((self.I + self.NaPart(self.m[i-1], self.h[i-1], self.V[i-1]) + self.KPart(self.n[i-1], self.V[i-1]) + self.ClPart(self.V[i-1])) / self.C)
            self.n[i] = self.n[i-1] + self.deltaT * (self.alpha_n(self.V[i]) * (1-self.n[i-1]) - self.beta_n(self.V[i])*self.n[i-1])
            self.m[i] = self.m[i-1] + self.deltaT * (self.alpha_m(self.V[i]) * (1-self.m[i-1]) - self.beta_m(self.V[i])*self.m[i-1])
            self.h[i] = self.h[i-1] + self.deltaT * (self.alpha_h(self.V[i]) * (1-self.h[i-1]) - self.beta_h(self.V[i])*self.h[i-1])
        plt.plot(self.time, self.V)
        plt.xlabel("Time")
        plt.ylabel("Membrane Potential in volts")
        plt.title("Membrane Potential of a Neuron over Time with Input Current =" +str(self.I))
        plt.show()


abc = HH(10)
abc.plotNeuronActivity()


