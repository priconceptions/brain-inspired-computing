# Neural Models and Spiking Neurons

As discussed in the previous articles, the membrane potential (measured in volts) changes because of the change in ion concentrations inside and outside a cell. The ability for a neuron to hold electric charge allows us to model the cell as a circuit, summarized in the equation below:

<img src="https://tex.s2cms.ru/svg/Q%20%3D%20V*C" alt="Q = V*C" />

* <img src="https://tex.s2cms.ru/svg/Q%20%3D%20" alt="Q = " /> differential distribution of electric charge across the membrane 
* <img src="https://tex.s2cms.ru/svg/V%20%3D%20" alt="V = " /> voltage difference between the intracellular and extracellular areas
* <img src="https://tex.s2cms.ru/svg/C%20%3D%20" alt="C = " /> the membrane capacitance (an intrinsic property of the cell that determines the cell's capacity to hold electric charge)

If a neuron had no ion channels, its behavior could be described by the equation above. However, the passage of ions is met with resistance and therefore, these ion channels can be represented as resistors. In fact, the voltage difference caused by the concentration differences can be modeled as a battery that sets the membrane potential for that neuron.

Many models capture the properties of a neuron and mathematically simulate it.

#### Integrate and Fire Model

This model tracks the change in the membrane potential as a function of the input current fed into the neuron. Given a constant capacitance <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7BC_m%7D" alt="\inline {C_m}" /> the input is integrated over time into the membrane potential.

<img src="https://tex.s2cms.ru/svg/C_%7Bm%7D%5Cfrac%20%7BdV%7D%7Bdt%7D%20%3D%20I(t)" alt="C_{m}\frac {dV}{dt} = I(t)" />

This model, however, is too simplistic in that inputs provided a long time ago are also integrated until the voltage reaches a threshold voltage <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7BV_%7Bth%7D%7D" alt="\inline {V_{th}}" /> at which point the voltage is set back to the resting voltage of membrane.

#### Leaky Integrate and Fire Model

This model is an extension of the integrate and fire model that is more biologically plausible. It adds a "leak term" to the membrane potential so that inputs provided a long time ago are not integrated. The model is as follows:

<img src="https://tex.s2cms.ru/svg/C_%7Bm%7D%20%5Cfrac%20%7BdV%7D%7Bdt%7D%20%3D%20I(t)%20-%20%5Cfrac%20%7BV_%7Bm%7D%20(t)%7D%7BR_%7Bm%7D%7D" alt="C_{m} \frac {dV}{dt} = I(t) - \frac {V_{m} (t)}{R_{m}}" />

Again, <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7BC_%7Bm%7D%7D" alt="\inline {C_{m}}" /> is the capacitance. <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7BR_%7Bm%7D%7D" alt="\inline {R_{m}}" /> is the membrane's resistance to leaks. Therefore, the input current has to reach the threshold of <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7BI_%7Bth%7D%20%3D%20%5Cfrac%20%7BV_%7Bth%7D%7D%7BR_%7Bm%7D%7D%7D" alt="\inline {I_{th} = \frac {V_{th}}{R_{m}}}" /> for the neuron to spike.

#### Hodgkin-Huxley Model



