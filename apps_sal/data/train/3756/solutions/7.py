import math


def goldbach_partitions(n):
    primes = []
    partitions = []
    if n % 2 != 0:
        return []
    for i in range(0, n + 1):
        if i > 1:
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    break
            else:
                primes.append(i)
    for i in primes:
        if i <= n / 2:
            if n - i in primes:
                partitions.append(str(i) + '+' + str(n - i))
    return partitions
