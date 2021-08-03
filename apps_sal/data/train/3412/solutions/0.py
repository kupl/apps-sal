def f(n):
    res = 1
    i = 2
    while n != 1:
        k = 0
        while n % i == 0:
            k += 1
            n //= i
        if k != 0:
            res *= k * i**(k - 1)
        i += 1
    return res
