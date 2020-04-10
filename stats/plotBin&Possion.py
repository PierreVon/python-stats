import matplotlib.pyplot as plt
from scipy import stats
import numpy as np


def b_p(n, p):
    bi = stats.binom(n, p)
    xb = np.arange(bi.ppf(.01), bi.ppf(.99))

    mu = n * p
    pois = stats.poisson(mu)
    xp = np.arange(pois.ppf(0.01), pois.ppf(0.99))

    print('---------Feature----------')
    mean, var, skew, kurt = bi.stats(moments='mvsk')
    print(mean, var, skew, kurt)
    mean, var, skew, kurt = pois.stats(moments='mvsk')
    print(mean, var, skew, kurt)

    plt.scatter(xb, bi.pmf(xb), label='binom pmf')
    plt.scatter(xp, pois.pmf(xp), label='poisson pmf')
    plt.legend(loc='best', frameon=False)
    plt.ylabel('Probability')
    plt.title('PMF of binomial distribution(n={}, p={}), poisson(lambda={})'.format(n, p, mu))


plt.subplot(211)
b_p(20, 0.6)
plt.subplot(212)
b_p(50, 0.08)
plt.show()
