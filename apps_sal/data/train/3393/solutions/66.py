import math


def get_divisors(n):
    i = 1
    result = []
    while i <= math.sqrt(n):
        if n % i == 0:
            if n / i == i:
                result.append(i)
            else:
                result += [i, n / i]
        i += 1
    return result


def get_squared(n):
    return [x * x for x in n]


def list_squared(m, n):
    pairs = [[x, sum(get_squared(get_divisors(x)))] for x in range(m, n + 1)]
    return list([x for x in pairs if math.sqrt(x[1]) % 1 == 0])
