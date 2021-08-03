import math
from _bisect import *


def factors(n):
    l = set()
    x = int(math.sqrt(n))
    for i in range(1, x + 1):
        if n % i == 0:
            l.add(i)
            if n // i != i:
                l.add(n // i)
    return l


for T in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    divisors = set()
    for i in range(n):
        divisors = divisors.union(factors(a[i]))
    divisors = list(divisors)
    divisors.sort()
    oneIndex = -1
    for i in range(len(divisors)):
        if divisors[i] == 1:
            oneIndex = i
            break
    dp = [0 for x in range(len(divisors))]
    for i in range(n):
        for j in range(len(divisors)):
            x = 0
            if a[i] == divisors[j]:
                x = 1
            y = math.gcd(a[i], divisors[j])
            ind = bisect_left(divisors, y)
            dp[ind] += (x + dp[j])
    print(dp[oneIndex])
