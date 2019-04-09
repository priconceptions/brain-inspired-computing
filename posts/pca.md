# Unsupervised Learning and Principle Component Analysis

As we discussed in previous articles, the Hebbian learning rule can be summarized by this equation:

<img src="https://tex.s2cms.ru/svg/w_%7Bji%7D(t%2B1)%20%3D%20w_%7Bji%7D(t)%20%2B%20%5Cepsilon%20x_%7Bj%7D(t)%20y_%7Bi%7D(t)" alt="w_{ji}(t+1) = w_{ji}(t) + \epsilon x_{j}(t) y_{i}(t)" />

Basically, according to the Hebbian learning rule, weights are updated when there is a concurrent activity in the pre-synaptic and post-synaptic neurons.

So, what capabilities does Hebbian learning give us?

* It allows us to detect correlations [^1] between inputs and outputs (of course!-- "Neurons that fire together wire together")
* It allows us to detect correlations between different inputs.
    * Inputs that are positively correlated have weights that are positively correlated
    * Inputs that are negatively correlated have weights that are negatively correlated

In the early 1960's, Horace Barlow came up with the idea of **redundancy reduction**, which is the process of transforming the input in a way that reduces redundancy that occurs because of statistical dependencies between the variables in the input stream.

We can use **Principle Component Analysis (PCA)** to do this. For example, if we had two inputs in the input stream <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7Bx_i%7D" alt="\inline {x_i}" /> and <img src="https://tex.s2cms.ru/svg/%5Cinline%20%7Bx_j%7D" alt="\inline {x_j}" /> that are correlated:

<img src="https://tex.s2cms.ru/svg/c_%7Bij%7D%20%3D%20%3Cx_%7Bi%7D%20x_%7Bj%7D%3E%20%5Cneq%200" alt="c_{ij} = &lt;x_{i} x_{j}&gt; \neq 0" />

the goal of PCA is to transform input **x** in such a way that these pairwise correlations are eliminated.


[^1]: A correlation in this context refers to a linear association between two variables or how close two variables are to having a linear relationship. It is the measure of how similar two variables' deviations from their respective means is. (Ranges from -1 to 1)










