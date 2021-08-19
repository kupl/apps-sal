import math


def squareDivisors(n):
    list_divisors = []
    i = 1
    while i <= math.sqrt(n):
        if (n % i == 0):
            # If divisors are equal, print only one
            if (n / i == i):
                list_divisors.append(i**2)
            else:
                # Otherwise print both
                list_divisors.extend([i**2, (n // i)**2])
        i = i + 1
    return list_divisors


def list_squared(m, n):
    return [[i, sum(squareDivisors(i))] for i in range(m, n + 1) if math.sqrt(sum(squareDivisors(i))).is_integer()]
