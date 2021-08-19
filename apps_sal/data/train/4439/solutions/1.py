def div_num(a, b):
    return 'Error' if a > b else sorted([i for i in range(a, b + 1)], key=lambda k: (-divisors(k), k))[0]


def divisors(n):
    d = {i for i in range(1, int(n ** 0.5 + 0.99)) if n % i == 0}
    return len(d | {n // i for i in d})
