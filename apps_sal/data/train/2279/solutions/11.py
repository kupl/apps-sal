import os
import io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n = 10 ** 6 + 1
primes = [1] * n
(primes[0], primes[1]) = (0, 0)
v = int(n ** 0.5) + 1
for i in range(2, v):
    if primes[i]:
        for j in range(i * i, n, i):
            primes[j] = 0
for i in range(1, n):
    primes[i] += primes[i - 1]
cases = int(input())
for t in range(cases):
    n1 = list(map(int, input().split()))
    for ni in n1:
        print(primes[ni] - primes[int(ni ** 0.5)] + 1)
