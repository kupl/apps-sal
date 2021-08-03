# 素因数分解
import sys


def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table


input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
# かけらを移動させて共通因数を持つようにする
su = sum(A)
if su == 1:
    print(-1)
    return
primes = list(set(prime_decomposition(su)))
ans = float("inf")
Idx1 = [i for i, a in enumerate(A) if a]

for p in primes:
    an = 0
    half = p // 2
    for t in zip(*[iter(Idx1)] * p):
        idx = t[half]
        an += sum(abs(i - idx) for i in t)
    ans = min(ans, an)
print(ans)
