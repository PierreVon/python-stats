from matplotlib import pyplot as plt
import numpy as np

# from matplotlib.font_manager import FontManager
# fm = FontManager()
# mat_fonts = set(f.name for f in fm.ttflist)
# print(mat_fonts)


plt.subplot(221)
# plt.subplot2grid((3, 3), (1, 0), colspan=2)

plt.plot([1, 2, 3, 4, 5], [3, 6, 2, 7, 6], 'r--', [1, 4, 3, 7], [2, 3, 6, 9], 'mp-')
plt.ylabel("y轴", fontproperties='Heiti TC', fontsize=10)
plt.title("测试", fontproperties='Heiti TC', fontsize=10)
plt.text(2, 4, r'$\mu=100$', fontsize=10)  # Latex
plt.annotate("(4, 3)", xy=(4, 3), xytext=(5, 4), arrowprops=dict(facecolor='black', shrink=0.1, width=2))  # Latex
plt.axis([1, 5, 1, 8])
plt.grid(True)
plt.savefig('a', dpi=600)

plt.subplot(222)
plt.pie([15, 30, 45, 10], explode=[0, 0.1, 0, 0], labels=['a', 'b', 'c', 'd'],
        autopct='%1.1f%%')
plt.axis('equal')

plt.subplot(223)
plt.hist(np.random.normal(100, 20, size=100), 10)


plt.show()
