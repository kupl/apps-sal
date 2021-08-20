def isprime(x):
    return next((0 for i in range(3, int(x ** 0.5) + 1, 2) if not x % i), 1)


def f(n):
    limit = len(str(n)) - 1 - (str(n)[0] == '1')
    return next((i for i in range(n - [1, 2][n & 1], 1, -2) if isprime(i) and sum([not int(k) & 1 for k in str(i)]) == limit))
