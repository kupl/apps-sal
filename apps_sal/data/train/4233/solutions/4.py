def isprime(x):
    return x > 1 and all((x % i for i in range(2, int(x ** 0.5) + 1)))


def goldbach(n):
    return [[i, n - i] for i in range(n // 2 + 1) if isprime(i) and isprime(n - i)]
