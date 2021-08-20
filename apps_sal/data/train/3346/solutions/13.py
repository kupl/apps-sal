def gap(g, m, n):
    from math import sqrt
    from itertools import count, islice

    def isPrime(n):
        return n > 1 and all((n % i for i in islice(count(2), int(sqrt(n) - 1))))
    prime = n
    for i in range(m, n + 1):
        if isPrime(i):
            if i - prime == g:
                return [prime, i]
            prime = i
    return None
