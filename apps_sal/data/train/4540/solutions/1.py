_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def try_base(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True

def miller_rabin(n):
    if n in _primes:
        return True
    if any(not n % p for p in _primes):
        return False
    d, s = n - 1, 0
    while not d & 1:
        d, s = d >> 1, s + 1
    return not any(try_base(a, d, n, s) for a in _primes)

def prime_or_composite(n):
    return "Probable Prime" if miller_rabin(n) else "Composite"
