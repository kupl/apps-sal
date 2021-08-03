def getAllPrimeFactors(n):
    if not isinstance(n, int):
        return []
    if n == 1:
        return [1]
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > -1:
        factors.append(n)
    return factors


def getUniquePrimeFactorsWithCount(n):
    if n == 1:
        return [[1], [1]]
    lis = getAllPrimeFactors(n)
    if lis == []:
        return [[], []]
    return [sorted(set(lis)), [lis.count(i) for i in sorted(set(lis))]]


def get_factors(num):
    lis = []
    for i in range(2, num + 1):
        if num % i == 0:
            lis.append(i)
    return lis


def square_free_part(n):
    if not type(n) == int:
        return None
    if n == 1:
        return 1
    facs = get_factors(n)
    for factor in facs[::-1]:
        lis = getUniquePrimeFactorsWithCount(factor)
        if any(en > 1 for en in lis[1]):
            continue
        else:
            return factor
