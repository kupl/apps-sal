import sys
import math
input = sys.stdin.readline
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
dic = {}
t = 0
for i in primes:
    dic[i] = t
    t += 1


def primeFactors(n, arr):
    while n % 2 == 0:
        arr[dic[2]] += 1
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            arr[dic[i]] += 1
            n = n / i

    if n > 2:
        arr[dic[n]] += 1
    return arr


def main():
    N = int(input())
    A = list(map(int, input().split()))
    tp = [0] * len(primes)
    dp = []
    dp.append(tp)
    for i in range(1, N + 1):
        r = dp[i - 1].copy()
        t = primeFactors(A[i - 1], r)
        dp.append(t)
    t = int(input())
    for _ in range(t):
        l, r, m = list(map(int, input().split()))
        if(m == 1):
            print(0)
        else:
            ans = 1
            for i in range(len(primes)):
                ans = ans * (pow(primes[i], dp[r][i] - dp[l - 1][i], m)) % m
            print(ans % m)


def __starting_point():
    main()


__starting_point()
