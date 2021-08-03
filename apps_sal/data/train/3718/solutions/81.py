def divisors(n):
    res = []
    i = 1
    while i <= n:
        if n % i == 0:
            res.append(i)
        i = i + 1
    return len(res)
