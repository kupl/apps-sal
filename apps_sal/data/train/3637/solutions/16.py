def num_primorial(n):
    primes = [2]
    i = 1
    new_p = 2
    while i < n:
        j = 0
        while j < len(primes):
            if new_p % primes[j] == 0:
                new_p += 1
                break
            else:
                j += 1
        if j == len(primes):
            primes = primes + [new_p]
            new_p += 1
            i += 1
    product = primes[0]
    for p in primes[1:]:
        product *= p
    return product
