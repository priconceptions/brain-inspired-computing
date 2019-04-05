# implementation of the Izhikevich model
import numpy as np
import matplotlib.pyplot as plt

class Izhikevich:
    def __init__(self, I = 1.5):
        self.I = I

        # all neuron properties
        self.totalTime = 500
        self.deltaT = 0.01
        self.time = np.arange(0, self.totalTime, self.deltaT)
        self.V = np.zeros(len(self.time))
        self.U = np.zeros(len(self.time))
        self.a = 0.02
        self.b = 0.2
        self.c = -65
        self.d = 2
        self.V_thresh = 30 # Threshold voltage
        self.V_spike = 0.5 #Spike delta
    
    def plotNeuronActivity(self):
        self.V[0] = -55
        for i in range(1, len(self.time)):
            self.V[i] = self.V[i-1] + self.deltaT * (0.04*((self.V[i-1])**2) + 5*self.V[i-1] + 140 - self.U[i-1] + self.I)
            self.U[i] = self.U[i-1] + self.deltaT * (self.a*(self.b*self.V[i] - self.U[i-1]))
            if self.V[i] >= self.V_thresh:
                self.V[i] = self.c
                self.U[i] = self.U[i] + self.d
        plt.plot(self.time, self.V)
        plt.xlabel("Time")
        plt.ylabel("Membrane Potential in volts")
        plt.title("Membrane Potential of a Neuron over Time with Input Current =" +str(self.I))
        plt.show()

    def plotSpikes(self):
        self.V[0] = -55
        spikes = []
        inputCurrent = np.arange(2, 30, 0.1)
        for current in inputCurrent:
            numSpikes = 0
            for i in range(1, len(self.time)):
                self.V[i] = self.V[i-1] + self.deltaT * (0.04*((self.V[i-1])**2) + 5*self.V[i-1] + 140 - self.U[i-1] + current)
                self.U[i] = self.U[i-1] + self.deltaT * (self.a*(self.b*self.V[i] - self.U[i-1]))
                if self.V[i] >= self.V_thresh:
                    self.V[i] = self.c
                    self.U[i] = self.U[i] + self.d
                    numSpikes += 1
            spikes.append(numSpikes/self.totalTime)
        plt.plot(inputCurrent, spikes)
        plt.xlabel("Input Current")
        plt.ylabel("Number of Spikes")
        plt.title("Frequency of spikes over different input currents")
        plt.show()

abc = Izhikevich(7)
abc.plotNeuronActivity()
abc.plotSpikes()