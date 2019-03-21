# Neural Anatomy

A neural cell is an entity that takes in input, processes the input, and produces an output. It can be thought of as an electric signal converter. A black box representation of a neural cell can be seen below:

![alt text](https://user-images.githubusercontent.com/13342705/54393724-442c7300-4681-11e9-8182-43e32e6face5.PNG "BlackBox representation of a neuron")
A biological neuron is obviously more complicated but at its core, does the same thing as the neuron in the picture above.

#### An Over-Simplified Illustration of a Biological Neuron

![alt text](https://cdn-images-1.medium.com/max/2400/1*1Oh53dNdPITVnoOVGCCUFA.png "The Biological Neuron - From Wikipedia (https://cdn-images-1.medium.com/max/2400/1*1Oh53dNdPITVnoOVGCCUFA.png)")

The neuron is the basic computing unit in our bodies and is the building block of our nervous system.

* **Dendrite**: The input receiver of a neuron-- propagates the electrochemical stimulation received from other cells.
* **Soma**: The cell body of the neuron-- contains all other neural organelles and processes information to send to other neurons.
* **Axon**: A long projection of the nerve cell that conducts signals from the soma. The ends of an axon, the purple projection are called axon terminals.
* **Synapse**: Space between neurons through which neurotransmitters transmit electrical signals from one neuron to other neurons.

Basically, a neuron takes in input from the dendrites, processes them in the soma (which acts as a CPU unit), and sends an output through the axon. 

Bundles of fibers hold neurons together to form nerves. Under a microscope, if the fibers are myelinated (myelin is a fatty substance that insulates the axon to enhance signal propagation) axons, they appear white, and therefore we call them white matter. On the other hand, areas of the fibers consist of somata and dendrites appear grey and we call them grey matter.

The nervous system comprises of networks made from neurons and synapses, successively forming levels of computation to allow organisms to learn, act, and live. Sterratt, D., Graham, B., Gillies, A., & Willshaw, D. (2011) classify neuroscience into nine levels, shown below, based on size and function.

| Level              | Size   | Descriptions and Functions                                                |
|--------------------|--------|---------------------------------------------------------------------------|
| Nervous system     | > 1 m  | Total system controlling thought, behavior, and sensory & motor functions |
| Subsystem          | 10 cm  | Subsystem associated with one or more functions                           |
| Neural Network     | 1 cm   | Neural networks for system, subsystem, and functions                      |
| Microcircuit       | 1 mm   | Networks of multilevel neurons, e.g., visual subsystem                    |
| Neuron             | 100 µm | Elementary biological unit of neuronal network                            |
| Debdric subunit    | 10 µm  | Arbor of receptors in neuron                                              |
| Synapse            | 1 µm   | Junction or connectivity between neurons                                  |
| Signalling pathway | 1 nm   | Link between connecting neurons                                           |
| Ion Channels       | 1 pm   | Channels that act as gateway causing voltage change                       |

Santiago Ramón y Cajal, a Spanish neuroscientist, won the Nobel Prize in Physiology or Medicine for first investigating the microscopic structure of the human brain and for discovering that the relationship between nerve cells was not continuous, but contiguous. This is now widely considered the basis of modern neuroscience.

Now, we can see neurons taking many different forms based on their functions:

![neuronTypes](https://user-images.githubusercontent.com/13342705/54726810-0cbf3a00-4b4b-11e9-90e3-397a807b7e30.PNG)

#### Elements of Neuron Electrophysiology

Much of the computational power that neurons possess lies in the electrical properties of the neurons. How do neurons generate this electrical power and send and receive electrical signals between each other?

All cells are bathed in a fluid called **extracellular fluid**, which provides a stable environment for cells to operate. It contains water, some inorganic ions, three main cations-- Sodium (Na+ = 136–145 mEq/L), Potassium (K+ = 3.5–5.5 mEq/L), and Calcium (Ca2+ = 2.2–2.6 mEq/L), and two main anions-- Chloride (Cl− = 99–109 mEq/L), Hydrogen Carbonate (HCO3− 22–26 mM).

In addition to the extracellular fluid, cells contain a fluid called **intracellular fluid**, which contains ions, water, and inorganic ions as well. However, the ionic concentration differs widely from that of extracellular fluid, causing an electric potential difference. This electric potential difference across the cell membrane is called **membrane potential**. The resting membrane potential of a neuron is typically -65mV where the potential inside the cell is more negative than the outside.

Ions penetrate the membrane through **ion channels** or openings in the cell membrane. When ion channels are in an **open state**, ions from the extracellular fluid are allowed to enter the cell. These channels can either be **active channels**, which can open or close because of certain stimuli or **passive channels**, which consistently remain. A schematic representation of the neuronal membrane is shown below:

![alt text](https://user-images.githubusercontent.com/13342705/54393725-442c7300-4681-11e9-88f8-a5ba8a1024ee.PNG "Ionic Channel")

The movement of ions between the membrane can be explained by Fick's law of diffusion that says:  
1. The flux (*J*) move from an area of high concentration to an area of low concentration.
2. Larger concentration differences cause larger fluxes.

So, Fick's law can be mathematically described as follows:

<img src="https://tex.s2cms.ru/svg/J%20%3D%20%7B-D%20%5Cdfrac%7B%5Cpartial%20%5Cvarphi%7D%7B%5Cpartial%20x%7D%7D" alt="J = {-D \dfrac{\partial \varphi}{\partial x}}" />

* *D* = diffusion coefficient
* <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7B%5Cvarphi%7D" alt="\inline {\varphi}" /> = Concentration
* *x* = single dimension (position)

This movement causes a change in the membrane potential. The membrane potential can be determined using the Nernst equation and the Goldman equation.

* Nernst equation:

<img src="https://tex.s2cms.ru/svg/%7BE_%7Bx%7D%20%3D%20%7B%5Cdfrac%7BRT%7D%7BzF%7D%7D%20ln%7B%5Cdfrac%7B%5BX%5D_%7Boutside%7D%7D%7B%5BX%5D_%7Binside%7D%7D%7D" alt="{E_{x} = {\dfrac{RT}{zF}} ln{\dfrac{[X]_{outside}}{[X]_{inside}}}" />  

   * <img src="https://tex.s2cms.ru/svg/%5Cinline%20E_%7Bx%7D" alt="\inline E_{x}" /> = Membrane potential
   * <img src="https://tex.s2cms.ru/svg/%5Cinline%20%20R" alt="\inline  R" /> = Gas constant (<img src="https://tex.s2cms.ru/svg/%5Cinline%208.314471%20%5Cdfrac%20%7BJ%7D%20%7Bmol%7D" alt="\inline 8.314471 \dfrac {J} {mol}" />)
   * <img src="https://tex.s2cms.ru/svg/%5Cinline%20%20T" alt="\inline  T" /> = Temperature (kelvin)
   * <img src="https://tex.s2cms.ru/svg/%5Cinline%20z" alt="\inline z" /> = Valence (charge of the ion <img src="https://tex.s2cms.ru/svg/%5Cinline%20x" alt="\inline x" />)
   * <img src="https://tex.s2cms.ru/svg/%5Cinline%20F" alt="\inline F" /> = Faraday's constant (<img src="https://tex.s2cms.ru/svg/%5Cinline%2096%2C485.3415%20%5Cdfrac%20%7BC%7D%20%7Bmol%7D" alt="\inline 96,485.3415 \dfrac {C} {mol}" />)
   * <img src="https://tex.s2cms.ru/svg/%5Cinline%20%5BX%5D_%7Boutside%2Finside%7D" alt="\inline [X]_{outside/inside}" /> = Concentration of ion inside and outside the cell

* Goldman Equation is derived from the Nernst equation:

<img src="https://tex.s2cms.ru/svg/%7BV%20%3D%20%7B%5Cdfrac%7BRT%7D%7BF%7D%7D%20ln%7B%5Cdfrac%7BP%5E%7B%2B%7D_%7BNa%7D%5BNa%5E%2B%5D_%7Boutside%7D%20%2B%20P%5E%7B%2B%7D_%7BK%7D%5BK%5E%2B%5D_%7Boutside%7D%20%2B%20P%5E%7B-%7D_%7BCl%7D%5BCl%5E-%5D_%7Binside%7D%7D%7BP%5E%7B%2B%7D_%7BNa%7D%5BNa%5E%2B%5D_%7Binside%7D%20%2B%20P%5E%7B%2B%7D_%7BK%7D%5BK%5E%2B%5D_%7Binside%7D%20%2B%20P%5E%7B-%7D_%7BCl%7D%5BCl%5E-%5D_%7Boutside%7D%7D%7D" alt="{V = {\dfrac{RT}{F}} ln{\dfrac{P^{+}_{Na}[Na^+]_{outside} + P^{+}_{K}[K^+]_{outside} + P^{-}_{Cl}[Cl^-]_{inside}}{P^{+}_{Na}[Na^+]_{inside} + P^{+}_{K}[K^+]_{inside} + P^{-}_{Cl}[Cl^-]_{outside}}}" />  

   * <img src="https://tex.s2cms.ru/svg/%5Cinline%20V" alt="\inline V" /> = Membrane potential
   * <img src="https://tex.s2cms.ru/svg/%5Cinline%20R" alt="\inline R" /> = Gas constant (<img src="https://tex.s2cms.ru/svg/%5Cinline%208.314471%20%5Cdfrac%20%7BJ%7D%20%7Bmol%7D" alt="\inline 8.314471 \dfrac {J} {mol}" />)
   * <img src="https://tex.s2cms.ru/svg/%5Cinline%20T" alt="\inline T" /> = Temperature (kelvin) 
   * <img src="https://tex.s2cms.ru/svg/%5Cinline%20z" alt="\inline z" /> = Valence (charge of the ion <img src="https://tex.s2cms.ru/svg/%5Cinline%20x" alt="\inline x" />)
   * <img src="https://tex.s2cms.ru/svg/F" alt="F" /> = Faraday's constant (<img src="https://tex.s2cms.ru/svg/%5Cinline%2096%2C485.3415%20%5Cdfrac%20%7BC%7D%20%7Bmol%7D" alt="\inline 96,485.3415 \dfrac {C} {mol}" />)
   * <img src="https://tex.s2cms.ru/svg/%5Cinline%20%5BX%5D_%7Boutside%2Finside%7D" alt="\inline [X]_{outside/inside}" /> = Concentration of the specific ion inside and outside the cell
   * <img src="https://tex.s2cms.ru/svg/%5Cinline%20P%5E%7B%2B%7D_%7BK%7D%2C%20P%5E%7B%2B%7D_%7BNa%7D%2C%20P%5E%7B-%7D_%7BCl%7D" alt="\inline P^{+}_{K}, P^{+}_{Na}, P^{-}_{Cl}" /> = 1, 0.03, 0.1 respectively. This is the permeability of a membrane to a particular ion

The above equations explain the membrane potential as a function of the concentration of particular ions inside and outside the cell. When the membrane potential exceeds a certain threshold, a spike occurs. A couple of models discussed in the next article address this mechanism. How is information encoded and decoded in these spikes? The following articles will discuss this also.