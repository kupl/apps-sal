def list_squared(m, n):
    result, divisors = [], {k: k * k + 1 for k in range(m, n + 1)}
    divisors[1] = 1
    for d in range(2, int(n ** .5) + 1):
        for k in range(max(d * d, m + -m % d), n + 1, d):
            divisors[k] += d * d
            if k / d != d:
                divisors[k] += (k / d) ** 2
    for k in range(m, n + 1):
        if not divisors[k] ** .5 % 1:
            result.append([k, divisors[k]])
    return result
