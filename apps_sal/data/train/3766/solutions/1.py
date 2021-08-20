from collections import Counter


def getAllPrimeFactors(n):
    if type(n) != int:
        return []
    (li, j) = ([], 2)
    while j * j <= n:
        if n % j:
            j += 1
            continue
        li.append(j)
        n //= j
    return li + [[n], []][n < 1]


def getUniquePrimeFactorsWithCount(n):
    r = Counter(getAllPrimeFactors(n))
    return [list(r.keys()), list(r.values())]


def getUniquePrimeFactorsWithProducts(n):
    return [i ** j for (i, j) in zip(*getUniquePrimeFactorsWithCount(n))]
