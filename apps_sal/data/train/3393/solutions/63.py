import math


def list_squared(m, n):
    result = []
    for i in range(m, n + 1):
        divisors = set()
        for j in range(1, int(math.sqrt(i) + 1)):
            if i % j == 0:
                divisors.add(j**2)
                divisors.add(int(i / j)**2)
        summa = sum(divisors)
        if (summa ** 0.5).is_integer():
            result.append([i, summa])
    return result
