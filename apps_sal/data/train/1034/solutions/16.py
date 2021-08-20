import sys
sys.setrecursionlimit(10000000)


def primeFactors(n):
    factors = []
    cnt = 0
    if n % 2 == 0:
        while n % 2 == 0:
            cnt += 1
            n = n // 2
        factors.append(2 ** cnt)
    for i in range(3, int(n ** 0.5) + 1, 2):
        cnt = 0
        if n % i == 0:
            while n % i == 0:
                cnt += 1
                n = n // i
            factors.append(i ** cnt)
    if n != 1:
        factors.append(n)
    return factors


def minSum(arr, k):
    if len(arr) == k:
        return sum(arr)
    ans = 1e+18
    for i in range(len(arr) - 1):
        temp = []
        for j in range(i + 1, len(arr)):
            temp = [arr[i] * arr[j]] + arr[:i] + arr[i + 1:j] + arr[j + 1:]
            ans = min(ans, minSum(temp, k))
    return ans


TC = int(input())
for tc in range(TC):
    (k, x) = list(map(int, input().strip().split()))
    factors = primeFactors(x)
    if len(factors) <= k:
        print(sum(factors) + k - len(factors))
    else:
        print(minSum(factors, k))
