from math import gcd
from itertools import groupby


def gcd_split(seq):
    gcds = [int(gcd(a, b) == 1) for a, b in zip(seq[1:], seq[:-1])]
    gcds.append(int(gcd(seq[0], seq[-1]) == 1))
    # print(gcds)
    if max(gcds) == 0:
        return -1
    else:
        splits = [len(list(x)) + 1 for num, x in groupby(gcds) if num == 0]
        # print(splits)
        if gcds[0] == gcds[-1] == 0:
            splits[0] += splits[-1] - 1
            splits = splits[:-1]
        return splits


for _ in range(int(input())):
    N = int(input())
    A = [int(x) for x in input().split()]
    split = gcd_split(A)
    # print(split)

    res = []
    if split != -1:
        for K in range(2, N + 1):
            temp = (x for x in split if x >= K)
            ins = sum([(x // (K - 1) - 1 if x % (K - 1) == 0 else x // (K - 1)) for x in temp])
            if ins == 0:
                break
            else:
                res.append(ins)
    else:
        for K in range(2, N + 1):
            ins = N // (K - 1) + (N % (K - 1) > 0)
            if ins == 0:
                break
            else:
                res.append(ins)

    res = res + [0] * (N - 1 - len(res))
    print(*res)
