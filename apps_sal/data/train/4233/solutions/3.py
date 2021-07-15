def isprime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) +1))

def goldbach(n):
    return [[a, b] for a, b in zip(range(1, n), range(n-1, 0, -1)) if a <= b and isprime(a) and isprime(b)]

