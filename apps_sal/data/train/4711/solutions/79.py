def zeros(n):
    # find the exponent of a prime factor p in the prime factorization of n!
    def find_exponent(n, p):
        factor = 0
        p_helper = p
        while n > p_helper:
            factor += int(n / p_helper)
            p_helper *= p
        return factor

    # trailing zeros correspond to divisibility by 10 and its powers
    # that can be deduced from divisibility by 2 and 5
    two_exponent = find_exponent(n, 2)
    five_exponent = find_exponent(n, 5)

    return min(two_exponent, five_exponent)
