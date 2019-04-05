# Neural Models and Spiking Neurons

As discussed in the previous articles, the membrane potential (measured in volts) changes because of the change in ion concentrations inside and outside a cell. The ability for a neuron to hold electric charge allows us to model the cell as a circuit, summarized in the equation below:

<img src="https://tex.s2cms.ru/svg/Q%20%3D%20V*C" alt="Q = V*C" />

* <img src="https://tex.s2cms.ru/svg/Q%20%3D%20" alt="Q = " /> differential distribution of electric charge across the membrane 
* <img src="https://tex.s2cms.ru/svg/V%20%3D%20" alt="V = " /> voltage difference between the intracellular and extracellular areas
* <img src="https://tex.s2cms.ru/svg/C%20%3D%20" alt="C = " /> the membrane capacitance (an intrinsic property of the cell that determines the cell's capacity to hold electric charge)

If a neuron had no ion channels, its behavior could be described by the equation above. However, the passage of ions is met with resistance and therefore, these ion channels can be represented as resistors. In fact, the voltage difference caused by the concentration differences can be modeled as a battery that sets the membrane potential for that neuron.

Many models capture the properties of a neuron and mathematically simulate it.

#### Integrate and Fire (IF) Model

This model tracks the change in the membrane potential as a function of the input current fed into the neuron. Given a constant capacitance <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7BC_m%7D" alt="\inline {C_m}" /> the input is integrated over time into the membrane potential.

<img src="https://tex.s2cms.ru/svg/C_%7Bm%7D%5Cfrac%20%7BdV%7D%7Bdt%7D%20%3D%20I(t)" alt="C_{m}\frac {dV}{dt} = I(t)" />

This model, however, is too simplistic in that inputs provided a long time ago are also integrated until the voltage reaches a threshold voltage <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7BV_%7Bth%7D%7D" alt="\inline {V_{th}}" /> at which point the voltage is set back to the resting voltage of membrane.

#### Leaky Integrate and Fire (LIF) Model

This model is an extension of the integrate and fire model that is more biologically plausible. It adds a "leak term" to the membrane potential so that inputs provided a long time ago are not integrated. The model is as follows:

<img src="https://tex.s2cms.ru/svg/C_%7Bm%7D%20%5Cfrac%20%7BdV%7D%7Bdt%7D%20%3D%20I(t)%20-%20%5Cfrac%20%7BV_%7Bm%7D%20(t)%7D%7BR_%7Bm%7D%7D" alt="C_{m} \frac {dV}{dt} = I(t) - \frac {V_{m} (t)}{R_{m}}" />

Again, <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7BC_%7Bm%7D%7D" alt="\inline {C_{m}}" /> is the capacitance. <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7BR_%7Bm%7D%7D" alt="\inline {R_{m}}" /> is the membrane's resistance to leaks. Therefore, the input current has to reach the threshold of <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7BI_%7Bth%7D%20%3D%20%5Cfrac%20%7BV_%7Bth%7D%7D%7BR_%7Bm%7D%7D%7D" alt="\inline {I_{th} = \frac {V_{th}}{R_{m}}}" /> for the neuron to spike.

Spikes generated from a simulation of a LIF neuron is shown below:

![LIFSpikes](https://user-images.githubusercontent.com/13342705/55572788-6a6c8e00-56d6-11e9-9668-21cb91cc4765.PNG)

#### Izhikevich Model

This model attempts to simulate the behavior of a neuron in a more biologically plausible way while maintaining the efficiency of a LIF or IF neuron. This model keeps track of two variables-- the membrane voltage (<img src="https://tex.s2cms.ru/svg/%5Cinline%20%7Bv%7D" alt="\inline {v}" />) and the membrane recovery variable (<img src="https://tex.s2cms.ru/svg/%5Cinline%20%7Bu%7D" alt="\inline {u}" />), which depends on four parameters. The model is as follows:

<img src="https://tex.s2cms.ru/svg/%5Cfrac%20%7Bdv%7D%7Bdt%7D%20%3D%200.04v%5E2%20%2B%205v%20%2B%20140%20-%20u%20%2B%20I" alt="\frac {dv}{dt} = 0.04v^2 + 5v + 140 - u + I" />

<img src="https://tex.s2cms.ru/svg/%5Cfrac%20%7Bdu%7D%7Bdt%7D%20%3D%20a(bv%20-%20u)" alt="\frac {du}{dt} = a(bv - u)" />

<img src="https://tex.s2cms.ru/svg/%20if%20v%20%3E%3D%2030%2C%20then%20%5Cbegin%7Bcases%7D%20v%20%3D%20c%20%5C%5C%20u%20%3D%20u%20%2B%20d%20%5Cend%7Bcases%7D" alt=" if v &gt;= 30, then \begin{cases} v = c \\ u = u + d \end{cases}" />

* <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7Bv%7D" alt="\inline {v}" /> is the membrane voltage
* <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7Bu%7D" alt="\inline {u}" /> is the membrane recovery variable
* Parameters: 
    * <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7Ba%7D" alt="\inline {a}" /> is the time scale of recovery variable <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7Bu%7D" alt="\inline {u}" />. Smaller values means slower recovery. Typically, <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7Ba%20%3D%200.02%7D" alt="\inline {a = 0.02}" />
    * <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7Bb%7D" alt="\inline {b}" /> is the sensitivity of recovery variable <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7Bu%7D" alt="\inline {u}" /> to fluctuations of membrane potential <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7Bv%7D" alt="\inline {v}" />. Typically, <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7Bb%20%3D%200.2%7D" alt="\inline {b = 0.2}" />
    * <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7Bc%7D" alt="\inline {c}" /> is the after spike reset value of membrane potential <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7Bv%7D" alt="\inline {v}" />. Typically, <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7Bc%20%3D%20-65%20mV%7D" alt="\inline {c = -65 mV}" />
    * <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7Bd%7D" alt="\inline {d}" /> is the after spike reset of recovery variable <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7Bu%7D" alt="\inline {u}" />. Typically <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7Bd%20%3D%202%7D" alt="\inline {d = 2}" />

The model is able to simulate the spiking behavior of a biological neuron while maintaining computational efficiency.

Spikes generated from a simulation of an Izhikevich neuron is shown below:

![IzhikevichSpikes](https://user-images.githubusercontent.com/13342705/55573060-fed6f080-56d6-11e9-82ff-85f44acaaa90.PNG)

#### Hodgkin-Huxley (H-H) Model

Of all the previous models, this is the most biologically plausible. The model is as follows:

<img src="https://tex.s2cms.ru/svg/C_%7Bm%7D%20%5Cfrac%20%7Bdv%7D%7Bdt%7D%20%3D%20I%20-%20g_%7BNa%7Dm%5E3h(v%20-%20v_%7BNa%7D)%20-%20g_%7BK%7Dn%5E4(v%20-%20v_K)%20-%20g_L(v%20-%20v_L)" alt="C_{m} \frac {dv}{dt} = I - g_{Na}m^3h(v - v_{Na}) - g_{K}n^4(v - v_K) - g_L(v - v_L)" />

* <img src="https://tex.s2cms.ru/svg/g_%7BNa%7D%2C%20g_%7BK%7D%2C%20and%20g_L" alt="g_{Na}, g_{K}, and g_L" /> are conductances (the inverse resitances of Na, K, and Cl respectively
* <img src="https://tex.s2cms.ru/svg/(v%20-%20v_%7Bx%7D)" alt="(v - v_{x})" /> is the difference between the membrane voltage and the equilibrium voltage <img src="https://tex.s2cms.ru/svg/v_%7Bx%7D" alt="v_{x}" />, where <img src="https://tex.s2cms.ru/svg/x" alt="x" /> is either Na, K, or Cl
* <img src="https://tex.s2cms.ru/svg/n%2C%20m%2C%20and%20h" alt="n, m, and h" /> are dimensionless quantities whose variation with time after a change in membrane potential is determined by:
    * <img src="https://tex.s2cms.ru/svg/%5Cfrac%20%7Bdn%7D%7Bdt%7D%20%3D%20%5Calpha_%7Bn%7D(1-n)%20-%20%5Cbeta_%7Bn%7Dn" alt="\frac {dn}{dt} = \alpha_{n}(1-n) - \beta_{n}n" /> 
        * <img src="https://tex.s2cms.ru/svg/%5Calpha_%7Bn%7D%20%3D%20%5Cfrac%20%7B0.01(v%2B10)%7D%20%7Be%5E%7B%5Cfrac%7Bv%2B10%7D%7B10%7D%7D%20-%201%7D" alt="\alpha_{n} = \frac {0.01(v+10)} {e^{\frac{v+10}{10}} - 1}" /> and <img src="https://tex.s2cms.ru/svg/%5Cbeta_%7Bn%7D%20%3D%200.125e%5E%7Bv%2F80%7D" alt="\beta_{n} = 0.125e^{v/80}" />
    * <img src="https://tex.s2cms.ru/svg/%5Cfrac%20%7Bdm%7D%7Bdt%7D%20%3D%20%5Calpha_%7Bm%7D(1-m)%20-%20%5Cbeta_%7Bm%7Dm" alt="\frac {dm}{dt} = \alpha_{m}(1-m) - \beta_{m}m" />
        * <img src="https://tex.s2cms.ru/svg/%5Calpha_%7Bm%7D%20%3D%20%5Cfrac%20%7B0.1(v%2B25)%7D%7Be%5E%7B%5Cfrac%20%7Bv%2B25%7D%7B10%7D%7D%20-%201%7D" alt="\alpha_{m} = \frac {0.1(v+25)}{e^{\frac {v+25}{10}} - 1}" /> and <img src="https://tex.s2cms.ru/svg/%5Cbeta_%7Bm%7D%20%3D%204e%5E%7Bv%2F18%7D" alt="\beta_{m} = 4e^{v/18}" />
    * <img src="https://tex.s2cms.ru/svg/%5Cfrac%20%7Bdh%7D%7Bdt%7D%20%3D%20%5Calpha_%7Bh%7D(1-h)%20-%20%5Cbeta_%7Bh%7Dh" alt="\frac {dh}{dt} = \alpha_{h}(1-h) - \beta_{h}h" />
        * <img src="https://tex.s2cms.ru/svg/%5Calpha_%7Bh%7D%20%3D%200.07e%5E%7Bv%2F20%7D" alt="\alpha_{h} = 0.07e^{v/20}" /> and <img src="https://tex.s2cms.ru/svg/%5Cbeta_%7Bh%7D%20%3D%20%5Cfrac%20%7B1%7D%7Be%5E%7B%5Cfrac%20%7Bv%2B30%7D%7B10%7D%7D%20%2B%201%7D" alt="\beta_{h} = \frac {1}{e^{\frac {v+30}{10}} + 1}" />













