def prime_bef_aft(num):
    m = 2 - (num%2 == 0)
    return [next(n for n in range(i, int(i*r), s) if is_prime(n)) for i, r, s in ((max(2, num-m), 0.8, -2), (num+m, 1.2, 2))]


def is_prime(n):
    factors = 0
    for k in (2, 3):
        while n % k == 0 and factors < 2:
            n //= k
            factors += 1
    k = 5
    step = 2
    while k * k <= n and factors < 2:
        if n % k:
            k += step
            step = 6 - step
        else:
            n //= k
            factors += 1
    if n > 1:
        factors += 1
    return factors == 1
