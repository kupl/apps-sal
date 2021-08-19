import itertools


def findsubsets(s, n):
    return tuple(itertools.combinations(s, n))


def xorfunc(low, hi, a):
    xor1 = 0
    for i in range(low, hi + 1):
        xor1 ^= a[i]
    if xor1 == 0:
        return hi - low
    else:
        return 0


t = int(input())
for i in range(t):
    n = int(input())
    a = input()
    a = a.split()
    a = [int(it) for it in a]
    xor = 0
    xorsum = []
    for i in a:
        xor ^= i
        xorsum.append(xor)
    interlist = [i for i in range(n)]
    interlist2 = findsubsets(interlist, 2)
    interlist2 = [xorfunc(i, j, a) for (i, j) in interlist2]
    print(sum(interlist2))
