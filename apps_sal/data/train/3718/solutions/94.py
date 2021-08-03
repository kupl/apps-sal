def divisors(n):
    import math
    res = set()
    max_divisor = int(math.sqrt(n))
    for i in range(1, max_divisor + 1):
        if n % i == 0:
            res.add(i)
            res.add(n / i)
    return len(res)
