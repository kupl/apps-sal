import math
from collections import defaultdict
import itertools

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    total = 0
    tmp = 0
    fact = math.factorial(n)
    for i in range(n):
        tmp += a[i]
    tmp *= (fact // n)
    i = 1
    k = 1
    while i <= n:
        total += (k * tmp)
        k *= 10
        i += 1
    print(total)
