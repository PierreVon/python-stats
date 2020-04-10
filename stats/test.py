import numpy as np
from scipy import stats

print(stats.chi2_contingency(np.array([[37, 49, 23], [150, 100, 57]]), correction=True))
print(stats.chi2_contingency(np.array([[37, 49, 23], [37, 49, 23]])))

x = np.array([1, 2, 3, 4, 5])
y = stats.norm.rvs(size=10)
print(stats.kstest(x, 'expon'))
print(stats.kstest(y, 'norm'))

data1 = [21, 12, 12, 23, 19, 13, 20, 17, 14, 19]
data2 = [12, 11, 8, 9, 10, 15, 16, 17, 10, 16]

print("-------正态性检验--------")
print("Shapiro-wilk test", stats.shapiro(data1))
print("normal test", stats.normaltest(data1))
print("ANDERSON-DARLING检验", stats.anderson(data1))
print("ks检验", stats.kstest(data1, 'norm'), '\n')

print("-------相关性检验--------")
print("卡方检验", stats.chi2_contingency(data1, data2))
print("皮尔逊检验", stats.pearsonr(data1, data2))
print("KENDALL秩相关系数", stats.kendalltau(data1, data2))
print("SPEARMAN相关系数", stats.spearmanr(data1, data2), '\n')

print("-------参数检验--------")
print("---**配对样本**---")
print("配对t检验", stats.ttest_rel(data1, data2))
print("---**独立样本**---")
print("t检验", stats.ttest_ind(data1, data2))
print("方差检验", stats.f_oneway(data1, data2), '\n')

print("-------非参数检验--------")
print("---**配对样本**---")
# 原假设是：两配对样本来自的两总体的分布无显著差异。
print("威尔科克森符号秩检验", stats.wilcoxon(data1, data2))
data3 = [10, 5, 8, 12, 17, 15, 6, 17, 12, 16]
# 原假设是：多个配对样本来自的多个总体分布无显著差异。
print("FRIEDMAN检验", stats.friedmanchisquare(data1, data2, data3))
print("---**独立样本**---")
# 原假设：两组独立样本来自的两总体分布无显著差异。
print("曼-惠特尼U检验", stats.mannwhitneyu(data1, data2))
# 原假设是：多个独立样本来自的多个总体的中位数无显著差异。
print("中位数检验", stats.median_test(data1, data2))
# 原假设是：多个独立样本来自的多个总体的分布无显著差异。
print("Kruskal-wallis H检验 K-W平均秩检验", stats.kruskal(data1, data2), '\n')

