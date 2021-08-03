def proper_fractions(n):
    if n == 1:
        return 0
    res = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n /= i
            res -= res / i
        i += 1
    if n > 1:
        res -= res / n
    return int(res)
