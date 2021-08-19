import math


def sieve(x):
    l = [0] * x
    h = int(math.sqrt(x))
    for i in range(2, h + 1):
        if l[i - 1] == 0:
            for j in range(i * i, x + 1, i):
                l[j - 1] = 1
    l1 = []
    for k in range(2, x + 1):
        if l[k - 1] == 0:
            l1.append(k)
    print(sum(l1) % 10)


def __starting_point():
    t = int(input())
    for i in range(t):
        n = int(input())
        sieve(n)


__starting_point()
