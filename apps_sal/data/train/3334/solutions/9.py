def reduce_fraction(fraction):
    # your code here
    def get_gcd(x, y):
        a = min(x, y)
        b = max(x, y)
        if a == 0:
            return b
        return get_gcd(a, b % a)
    gcd = get_gcd(fraction[0], fraction[1])

    return tuple([int(x / gcd) for x in fraction])
