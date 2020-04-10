from scipy import stats
import numpy as np

# rvs: Random Variates
# pdf: Probability Density Function
# cdf: Cumulative Distribution Function
# sf: Survival Function (1-CDF)
# ppf: Percent Point Function (Inverse of CDF)
# isf: Inverse Survival Function (Inverse of SF)
# stats: Return mean, variance, (Fisher’s) skew, or (Fisher’s) kurtosis
# moment: non-central moments of the distribution
n = stats.norm(loc=3, scale=4)  # loc = mu, scale = sigma
print(n.cdf([1, 2, 3]))
print(n.mean(), n.std(), n.var())
print(n.ppf(0.5))
print(n.rvs(4))
print(n.sf(4), n.cdf(4))

print(stats.expon.mean(scale=3.))  # scale = 1. / lambda

print(stats.uniform.cdf([0, 1, 2, 3, 4, 5], loc=1, scale=4))
