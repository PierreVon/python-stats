def yT(n):
    i = 0
    while i < n:
        yield i
        i += 1


for i in yT(5):
    print(i)
