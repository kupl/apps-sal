def zeros(n):

    def find_exponent(n, p):
        factor = 0
        p_helper = p
        while n > p_helper:
            factor += int(n / p_helper)
            p_helper *= p
        return factor
    five_exponent = find_exponent(n, 5)
    return five_exponent
