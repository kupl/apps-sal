def getAllPrimeFactors(n):
    if type(n) is not int or n < 1:
        return []
    elif n < 3:
        return [n]
    factors = []
    while n > 1:
        for i in range(2, n + 1):
            if is_prime(i) and not n % i:
                factors.append(i)
                n = int(n / i)
                break
    return factors


def getUniquePrimeFactorsWithCount(n):
    f = getAllPrimeFactors(n)
    factors = list(set(f))
    powers = [f.count(factor) for factor in factors]
    return [factors, powers]


def getUniquePrimeFactorsWithProducts(n):
    cf = getUniquePrimeFactorsWithCount(n)
    return [factor**count for factor, count in zip(cf[0], cf[1])]


def is_prime(n):
    for i in range(2, n):
        if not n % i:
            return False
    return True
