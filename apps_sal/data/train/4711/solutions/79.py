def zeros(n):
    def find_exponent(n, p):
        factor = 0
        p_helper = p
        while n > p_helper:
            factor += int(n / p_helper)
            p_helper *= p
        return factor

    two_exponent = find_exponent(n, 2)
    five_exponent = find_exponent(n, 5)

    return min(two_exponent, five_exponent)
