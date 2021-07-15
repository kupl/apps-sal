def mul_power(n, k):
    res = 1
    i = 2
    while n != 1:
        d = 0
        while n%i == 0:
            n /= i
            d += 1
        if d%k:
            res = res*(i**(k-(d%k)))
        i += 1
    return res
