import math


def primes(n):
    maxPrime = -1
    while n % 2 == 0:
        maxPrime = 2
        n >>= 1
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n / i
    if n > 2:
        maxPrime = n
    return int(maxPrime)


def prtable(n):
    dp = [0 for i in range(n + 1)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    for i in range(4, n + 1):
        dp[i] = primes(i)
    return dp


pr = prtable(100000)
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if pr[a[i]] in d:
            d[pr[a[i]]] += 1
        else:
            d[pr[a[i]]] = 1
    ans = 0
    maxx = 0
    for i in d:
        if d[i] > ans:
            ans = d[i]
            maxx = i
        elif d[i] == ans:
            if maxx < i:
                maxx = i
                ans = d[i]
    print(maxx)
