import math


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def num_primorial(n):
    (s, j) = (1, 0)
    for i in range(2, n ** 2):
        if isPrime(i):
            s *= i
            j += 1
            if j == n:
                return s
