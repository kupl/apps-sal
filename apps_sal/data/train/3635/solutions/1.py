def sflpf_data(val, limit):
    result = []
    for n in range(4, limit + 1):
        factors = prime_factors(n)
        if len(factors) > 1 and min(factors) + max(factors) == val:
            result.append(n)
    return result


def prime_factors(n):
    factors = []
    while not n % 2:
        factors.append(2)
        n = n // 2
    while not n % 3:
        factors.append(3)
        n = n // 3
    k = 5
    step = 2
    while k <= n ** 0.5:
        if not n % k:
            factors.append(k)
            n = n // k
        else:
            k = k + step
            step = 6 - step
    factors.append(n)
    return factors
