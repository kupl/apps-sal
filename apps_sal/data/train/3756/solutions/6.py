def prime(givenNumber):
    primes = []
    for possiblePrime in range(2, givenNumber + 1):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return primes


def goldbach_partitions(n):
    if n % 2 != 0:
        return []
    else:
        p = prime(n)
        res = []
        for i in p:
            if n - i in p:
                res.append('{}+{}'.format(i, n - i))
                p.remove(n - i)
        return res
