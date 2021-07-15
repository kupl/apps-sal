from functools import reduce
primes = [2, 3, 5, 7, 11, 13, 17]

def gen_primes():
    for p in primes:
        yield p

    next_prime = primes[-1]
    limit = int(next_prime ** 0.5) + 1
    while True:
        next_prime += 2
        if limit * limit < next_prime:
            limit += 2
        for p in primes:
            if next_prime % p == 0:
                break
            if p > limit:
                primes.append(next_prime)
                yield next_prime
                break

def gen_prime_factor_multiplicities(n):
    for p in gen_primes():
        count = 0
        while n % p == 0:
            count += 1
            n /= p
        if count > 0:
            yield (p, count)
        if n == 1:
            break

def min_special_mult(arr):
    bad = []
    good = []
    for a in arr:
        try:
            if a is not None:
                good.append(int(a))
        except:
            bad.append(a)
    if bad:
        if len(bad) == 1:
            return "There is 1 invalid entry: {}".format(bad[0])
        return "There are {} invalid entries: {}".format(len(bad), bad)

    maxes = {}
    for n in good:
        for p, m in gen_prime_factor_multiplicities(abs(n)):
            maxes[p] = max(maxes.get(p, m), m)
    factors = [p ** m for p, m in maxes.items()]
    return reduce(lambda a, b: a * b, factors)
    

