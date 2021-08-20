import math


def listsum(l):
    a = []
    for i in l:
        a = a + i
    return a


n = int(input())
m = math.ceil(math.sqrt(n))
a = [' '.join([str(m - i + x * m) for x in range(int((n - m + i) / m) + 1)]) for i in range(m)]
print(' '.join(a))
