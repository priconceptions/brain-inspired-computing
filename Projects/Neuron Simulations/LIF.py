# simulation of LIF neuron
import numpy as np
import matplotlib.pyplot as plt

class LIFNeuron:
    def __init__(self, inputCurrent = 1.5):
        self.inputCurrent = inputCurrent
        
        
        # all neuron properties
        self.totalTime = 100
        self.deltaT = 0.01
        self.time = np.arange(0, self.totalTime, self.deltaT)
        self.V_m = np.zeros(len(self.time))
        self.R_m = 1   # Resistance 
        self.C_m = 10  # Capacitance
        self.tau = self.R_m * self.C_m 
        self.V_thresh = 1 # Threshold voltage
        self.V_spike = 0.5 #Spike delta

    def plotNeuronActivity(self):
        for i in range(1, len(self.time)):
            self.V_m[i] = self.V_m[i-1] + self.deltaT * ((-self.V_m[i-1] + self.R_m*self.inputCurrent) / self.tau)
            if self.V_m[i] >= self.V_thresh:
                self.V_m[i-1] = self.V_m[i-1] + self.V_spike
                self.V_m[i] = 0
        plt.plot(self.time, self.V_m)
        plt.xlabel("Time")
        plt.ylabel("Membrane Potential in volts")
        plt.title("Membrane Potential of a Neuron over Time with Input Current =" +str(self.inputCurrent))
        plt.show()
    
    def plotSpikes(self):
        spikes = []
        inputCurrent = np.arange(1, 5, 0.05)
        for current in inputCurrent:
            numSpikes = 0
            for i in range(1, len(self.time)):
                self.V_m[i] = self.V_m[i-1] + self.deltaT * ((-self.V_m[i-1] + self.R_m*current) / self.tau)
                if self.V_m[i] >= self.V_thresh:
                    self.V_m[i-1] = self.V_m[i-1] + self.V_spike
                    self.V_m[i] = 0
                    numSpikes += 1
            spikes.append(numSpikes/self.totalTime)
        plt.plot(inputCurrent, spikes)
        plt.xlabel("Input Current")
        plt.ylabel("Number of Spikes")
        plt.title("Frequency of spikes over different input currents")
        plt.show()
                    


a = LIFNeuron(1.5)
a.plotNeuronActivity()
a.plotSpikes()

