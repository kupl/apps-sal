from collections import defaultdict
from math import log2
import bisect
from bisect import bisect_left, bisect_right
import sys
from math import gcd, sqrt
sys.setrecursionlimit(10**7)
inf = float("inf")
# n=int(input())
# n,m=map(int,input().split())
# l=list(map(int,input().split()))


def get_factors(x):
    if x == 1:
        return []
    sqrta = int(sqrt(x)) + 1
    for i in range(2, sqrta):
        if x % i == 0:
            return [i] + get_factors(x // i)
    return [x]


def min_generator(fac, k, index, new_list):
    if index == len(fac):
        return sum(new_list)
    mina = inf
    for i in range(0, min(index + 1, len(new_list))):
        new_list[i] *= fac[index]
        theta = min_generator(fac, k, index + 1, new_list)
        if theta < mina:
            mina = theta
        new_list[i] //= fac[index]
    return mina


def fun(k, x):
    dict = defaultdict(lambda: 1)
    factors = get_factors(x)
    for i in factors:
        dict[i] *= i
    if len(dict) == k:
        print(sum(dict.values()))
        return
    if len(dict) < k:
        suma = sum(dict.values())
        left = k - len(dict)
        suma += left
        print(suma)
        return
    if k == 1:
        print(x)
        return
    fac = list(dict.values())

    new_list = [1] * k
    theta = min_generator(fac, k, 0, new_list)
    print(theta)


for i in range(int(input())):
    k, x = map(int, input().split())
    fun(k, x)
