import numpy as np

print("\n# basic #")
a = np.array([[1, 2, 3],
              [2, 3, 4]])
print(a ** 2)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
print(a.itemsize)

print(np.arange(5))
print(np.linspace(1, 10, 4))
print(np.linspace(1, 10, 4, endpoint=False))

a = np.concatenate((np.linspace(1, 10, 4), np.linspace(1, 10, 4, endpoint=False)))
print(a)
print(a.reshape((2, 4)))
a.resize((4, 2))
print(a.flatten())
print(a.astype(np.int))
print(a.tolist())

print(np.ones((2, 3)))
print(np.full((2, 3), 7))
print(np.eye(2))

print("\n# index #")
print(a.flatten()[1:4:2])
print(a[1, 0])
print(a[:, 1])
# leap
print(a[::2, 1])

print("\n# operation #")
print(a.mean())
print(a / a.mean())

print(np.abs(a))
print(np.sqrt(a))
print(np.square(a))
print(np.log(a))
print(np.ceil(a / a.mean()))
print(np.floor(a / a.mean()))

print(np.mod(a, np.ceil(a / a.mean())))

# 1, 2 dim
np.savetxt('a.csv', a, '%.2f', delimiter=',')
a = np.loadtxt('a.csv', dtype=np.float, delimiter=',')
print(a)

a.tofile('a.dat', sep=',', format='%.2f')
# a.tofile('a.dat', format='%.2f') 二进制
a = np.fromfile('a.dat', dtype=np.float, count=-1, sep=',')
print(a)

np.save('a.npy', a)
a = np.load('a.npy')
print(a)

print("\n# random #")
np.random.seed(10)
print(np.random.rand(2, 2))
# normal
print(np.random.randn(2, 2))
print(np.random.randint(1, 10, (2, 2)))

print(np.random.choice(a, 2, replace=False))
print(np.random.normal(1, 0.2, 10))
print(np.random.uniform(1, 10, (2, 10)))

print("\n# statistic #")
a.resize((4, 2))
print(np.sum(a))
print(np.mean(a, axis=0))
print(np.average(a, axis=0, weights=[1, 2, 1, 2]))

print(np.gradient(a))

print(np.r_[3, [0] * 5, -1:1:10j])
print(np.mgrid[0:5, 0:5])
print(np.poly1d([3, 4, 5]))
