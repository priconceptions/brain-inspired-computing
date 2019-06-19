# Neural Encoding and Decoding

Neurons have the unique ability to propagate information rapidly over long distances. An input a neuron receives varies drastically. Neurons can process sensory inputs from the environment like light, sound, touch, and smell as well as chemical and electrical inputs from inside the body. These stimuli are eventually converted into spikes, through which information is disseminated, decoded, and responded.

Neural encoding is the process of linking stimuli to neural responses. It is essential to understand how different stimuli can be understood and interpreted by neurons and how these neurons might react to different stimuli in order to model neural processes.

For the purposes of this article, we will go through a common problem-- the interpretation of a black-and-white 8 from the MNIST dataset:

![encoding_8](https://user-images.githubusercontent.com/13342705/56474862-ec3a1680-644d-11e9-8fa0-98ffd7eb52a0.PNG)

Neurons may interpret the image above in a few different ways.

#### Rate Encoding
Rate encoding means that the frequency of neuronal firing increases directly proportional to the intensity of the stimulus. So, with the image above, a rate encoded interpretation could be as follows:

![encoding_8_rate](https://user-images.githubusercontent.com/13342705/59797132-fee59600-92ac-11e9-9c29-e13d68677812.PNG)

Each pixel is encoded with neuron firing rates that increase in proportion to the color intensity of that particular pixel.

With this method, the timing of the spikes does not matter. We only count the number of spikes that the particular neuron generates over a fixed time interval. Over a period of 33 milliseconds, neuronal spike-generation could look like something below:

![RateEncoding](https://user-images.githubusercontent.com/13342705/59797569-fb064380-92ad-11e9-876c-be4445ba27ec.PNG)

During rate encoding, we usually calculate the firing rate by averaging procedures, like an average over time or an average over several runs of the experiment.

Rate encoding was first proposed by E.D. Adrian and Y. Zotterman in 1926. In their experiment, different weights were hung from a muscle. As the weights increased, the spikes generated from the sensory neurons innervating the muscle also increased.

This is a valid method of encoding information because of its simplicity. However, in scale, encoding information this way could be time-consuming and energy inefficient because spike generation is an expensive computational process. Also, this method completely disregards any information contained in the timing of the spikes.

#### Temporal Encoding



#### References
* Adrian ED, Zotterman Y (1926). "The impulses produced by sensory nerve endings: Part II: The response of a single end organ". J Physiol. 61 (2): 151–171. doi:10.1113/jphysiol.1926.sp002281. PMC 1514782. PMID 16993780