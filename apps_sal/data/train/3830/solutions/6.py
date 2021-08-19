from collections import defaultdict


def derivate(x):
    divisors = defaultdict(int)
    n = x
    i = 2
    while i * i <= x:
        while x % i == 0:
            divisors[i] += 1
            x /= i
        i += 1
    if x > 1:
        divisors[x] += 1
    if len(divisors) < 2:
        return 1
    return sum((k * n / p for (p, k) in divisors.items()))


def chain_arith_deriv(start, k):
    result = [start]
    for i in range(k - 1):
        result.append(derivate(result[-1]))
        if len(result) == 2 and result[-1] == 1:
            return '%d is a prime number' % start
    return result
