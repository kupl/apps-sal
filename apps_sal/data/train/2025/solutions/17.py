import math
import itertools
n = int(input())
primes = [2]
primes_degrees = []
for i in range(3, n + 1):
    for p in itertools.takewhile(lambda x: x <= i ** 0.5, primes):
        if i % p == 0:
            k = i // p
            while k > 1:
                if k % p != 0:
                    break
                k = k // p
            else:
                primes_degrees.append(i)
            break
    else:
        primes.append(i)
if n == 1:
    print(0)
else:
    print(len(primes) + len(primes_degrees))
    for p in primes:
        print(p, end=' ')
    for pd in primes_degrees:
        print(pd, end=' ')
