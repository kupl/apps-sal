import math
t = int(input())


def t_min(li, k):
    x = 0
    for i in range(k):
        x += li[i]
    return x


def cnt(li, x):
    n = 0
    for i in li:
        if x == i:
            n += 1
    return n


def num_of_occur(li, k):
    z = li[k - 1]
    y = 0
    for i in range(k):
        if li[i] == z:
            y += 1
    return y


def factorials(z, y):
    return math.factorial(z) / (math.factorial(y) * math.factorial(z - y))


for a in range(t):
    (n, k) = [int(x) for x in input().split()]
    lis = [int(x) for x in input().split()]
    lis.sort()
    sumn = t_min(lis, k)
    y = num_of_occur(lis, k)
    z = cnt(lis, lis[k - 1])
    print(int(factorials(z, y)))
