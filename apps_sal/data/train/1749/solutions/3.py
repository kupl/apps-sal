def trailing_zeros(number, base):
    smallest_prime_by_pow = {}
    p = 2
    b = base
    while b > 1 and p * p <= base:
        count_p_pow = 0
        while b % p == 0:
            count_p_pow += 1
            b //= p

        if count_p_pow:
            smallest_prime_by_pow[count_p_pow] = p

        p += 1 if p == 2 else 2

    if b > 1:
        smallest_prime_by_pow[1] = b

    res = number

    for count_p_pow, p in list(smallest_prime_by_pow.items()):
        count_p_in_fact = 0
        f = p
        while f <= number:
            count_p_in_fact += number // f
            f *= p

        res = min(res, count_p_in_fact // count_p_pow)

    return res
