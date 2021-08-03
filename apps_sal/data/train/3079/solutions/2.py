import math


def primecheck(num):
    a = math.sqrt(num)
    for i in range(2, int(a + 2)):
        if num % i == 0:
            return False
    return True


print(primecheck(25))


def big_primefac_div(n):
    if int(n) != n:
        return "The number has a decimal part. No Results"
    n = abs(n)
    factor = []
    prime = []
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            factor.append(i)
            factor.append(n / i)
    for j in factor:
        if primecheck(j) is True:
            prime.append(j)
    if len(factor) == 0:
        return []
    factor.sort()
    prime.sort()
    return [int(prime[-1]), int(factor[-1])]
