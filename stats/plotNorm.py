import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

norm = stats.norm(loc=2, scale=5)
x = np.linspace(-10, 20, 100)

pdf = norm.pdf(x)
cdf = norm.cdf(x)
print(norm.interval(0.90))
print(stats.normaltest(pdf))

plt.subplot(211)
plt.plot(x, pdf, label='pdf')
plt.ylabel('Probability')
plt.title(r'PDF/CDF of normal distribution')
plt.text(-10.0, .07, r'$\mu=2,\ \sigma=5$')
plt.legend(loc='best', frameon=False)
plt.subplot(212)
plt.plot(x, cdf, 'r-', label='cdf')
plt.ylabel('Probability')
plt.legend(loc='best', frameon=False)
plt.show()
