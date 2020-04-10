import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

xp = stats.expon()
x = np.linspace(0, 10, 100)
pdf = xp.pdf(x)
cdf = xp.cdf(x)

plt.plot(x, pdf)
plt.plot(x, cdf)
plt.show()
