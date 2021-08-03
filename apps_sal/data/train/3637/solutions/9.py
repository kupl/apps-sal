def num_primorial(n):
    def isprime(p):
        return p > 1 and all(p % i > 0 for i in range(2, int(p**.5 + 1)))
    primorial, p, c = 1, 1, 0
    while c < n:
        if isprime(p):
            primorial *= p
            c += 1
        p += 1
    return primorial
