def getAllPrimeFactors(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif type(n) != int:
        return errora
    elif n < 0:
        return errora
    allfacts = []
    current = 2
    n_copy = n
    while current <= n:
        if n_copy % current == 0:
            allfacts.append(current)
            n_copy /= current
        else:
            current += 1
    return allfacts


def getUniquePrimeFactorsWithCount(n):
    if type(n) != int:
        return errorb
    elif n < 0:
        return errorb
    primes = []
    power = []
    listA = getAllPrimeFactors(n)
    for i in range(len(listA)):
        if listA[i] not in primes:
            primes.append(listA[i])
            power.append(1)
        else:
            power[-1] += 1
    return [primes, power]


def getUniquePrimeFactorsWithProducts(n):
    if type(n) != int:
        return errorc
    elif n < 0:
        return errorc
    listlist = getUniquePrimeFactorsWithCount(n)
    listc = []
    for i in range(len(listlist[0])):
        listc.append(listlist[0][i] ** listlist[1][i])
    return listc


errora = []
errorb = [[], []]
errorc = []
