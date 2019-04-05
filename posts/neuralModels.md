# Neural Models and Spiking Neurons

As discussed in the previous articles, the membrane potential (measured in volts) changes because of the change in ion concentrations inside and outside a cell. The ability for a neuron to hold electric charge allows us to model the cell as a circuit, summarized in the equation below:

$$Q = V*C$$

* $$Q = $$ differential distribution of electric charge across the membrane 
* $$V = $$ voltage difference between the intracellular and extracellular areas
* $$C = $$ the membrane capacitance (an intrinsic property of the cell that determines the cell's capacity to hold electric charge)

If a neuron had no ion channels, its behavior could be described by the equation above. However, the passage of ions is met with resistance and therefore, these ion channels can be represented as resistors. In fact, the voltage difference caused by the concentration differences can be modeled as a battery that sets the membrane potential for that neuron.

Many models capture the properties of a neuron and mathematically simulate it.

#### Integrate and Fire (IF) Model

This model tracks the change in the membrane potential as a function of the input current fed into the neuron. Given a constant capacitance $$\inline {C_m}$$ the input is integrated over time into the membrane potential.

$$C_{m}\frac {dV}{dt} = I(t)$$

This model, however, is too simplistic in that inputs provided a long time ago are also integrated until the voltage reaches a threshold voltage $$\inline {V_{th}}$$ at which point the voltage is set back to the resting voltage of membrane.

#### Leaky Integrate and Fire (LIF) Model

This model is an extension of the integrate and fire model that is more biologically plausible. It adds a "leak term" to the membrane potential so that inputs provided a long time ago are not integrated. The model is as follows:

$$C_{m} \frac {dV}{dt} = I(t) - \frac {V_{m} (t)}{R_{m}}$$

Again, $$\inline {C_{m}}$$ is the capacitance. $$\inline {R_{m}}$$ is the membrane's resistance to leaks. Therefore, the input current has to reach the threshold of $$\inline {I_{th} = \frac {V_{th}}{R_{m}}}$$ for the neuron to spike.

Spikes generated from a simulation of a LIF neuron is shown below:

![LIFSpikes](https://user-images.githubusercontent.com/13342705/55572788-6a6c8e00-56d6-11e9-9668-21cb91cc4765.PNG)

#### Izhikevich Model

This model attempts to simulate the behavior of a neuron in a more biologically plausible way while maintaining the efficiency of a LIF or IF neuron. This model keeps track of two variables-- the membrane voltage ($$\inline {v}$$) and the membrane recovery variable ($$\inline {u}$$), which depends on four parameters. The model is as follows:

$$\frac {dv}{dt} = 0.04v^2 + 5v + 140 - u + I$$

$$\frac {du}{dt} = a(bv - u)$$

$$ if v >= 30, then \begin{cases} v = c \\ u = u + d \end{cases}$$

* $$\inline {v}$$ is the membrane voltage
* $$\inline {u}$$ is the membrane recovery variable
* Parameters: 
    * $$\inline {a}$$ is the time scale of recovery variable $$\inline {u}$$. Smaller values means slower recovery. Typically, $$\inline {a = 0.02}$$
    * $$\inline {b}$$ is the sensitivity of recovery variable $$\inline {u}$$ to fluctuations of membrane potential $$\inline {v}$$. Typically, $$\inline {b = 0.2}$$
    * $$\inline {c}$$ is the after spike reset value of membrane potential $$\inline {v}$$. Typically, $$\inline {c = -65 mV}$$
    * $$\inline {d}$$ is the after spike reset of recovery variable $$\inline {u}$$. Typically $$\inline {d = 2}$$

The model is able to simulate the spiking behavior of a biological neuron while maintaining computational efficiency.

Spikes generated from a simulation of an Izhikevich neuron is shown below:

![IzhikevichSpikes](https://user-images.githubusercontent.com/13342705/55573060-fed6f080-56d6-11e9-82ff-85f44acaaa90.PNG)

#### Hodgkin-Huxley (H-H) Model

Of all the previous models, this is the most biologically plausible. The model is as follows:

$$C_{m} \frac {dv}{dt} = I - g_{Na}m^3h(v - v_{Na}) - g_{K}n^4(v - v_K) - g_L(v - v_L)$$

* $$g_{Na}, g_{K}, and  g_L$$ are conductances (the inverse resitances of Na, K, and Cl respectively
* $$(v - v_{x})$$ is the difference between the membrane voltage and the equilibrium voltage $$v_{x}$$, where $$x$$ is either Na, K, or Cl
* $$n, m, and h$$ are dimensionless quantities whose variation with time after a change in membrane potential is determined by:
    * $$\inline {\frac {dn}{dt} = \alpha_{n}(1-n) - \beta_{n}n}$$ 
        * $$\inline {\alpha_{n} = \frac {0.01(v+10)} {e^{\frac{v+10}{10}} - 1}}$$ and $$\inline{\beta_{n} = 0.125e^{v/80}}$$
    * $$\inline {\frac {dm}{dt} = \alpha_{m}(1-m) - \beta_{m}m}$$
        * $$\inline {\alpha_{m} = \frac {0.1(v+25)}{e^{\frac {v+25}{10}} - 1}}$$ and $$\inline {\beta_{m} = 4e^{v/18}}$$
    * $$\inline {\frac {dh}{dt} = \alpha_{h}(1-h) - \beta_{h}h}$$
        * $$\inline {\alpha_{h} = 0.07e^{v/20}}$$ and $$\inline {\beta_{h} = \frac {1}{e^{\frac {v+30}{10}} + 1}}$$

Spikes generated by a simulation of an H-H neuron is below:
![HHSpikes](https://user-images.githubusercontent.com/13342705/55631035-1b316680-5785-11e9-9afb-44675bf3dbb3.PNG)

