def prime_bef_aft(num):
    m = 2 - (num % 2 == 0)
    b, a, p_b, p_a = 2 if num == 3 else num - m, num + m, False, False
    while not p_b or not p_a:
        p_b, b = (True, b) if p_b or is_prime(b) else (False, b - 2)
        p_a, a = (True, a) if p_a or is_prime(a) else (False, a + 2)
    return [b, a]


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
