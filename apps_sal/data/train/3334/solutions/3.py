def gcd(a, b):
    if not a%b:
        return b
    else:
        return gcd(b, a%b)

def reduce_fraction(fraction):
    return tuple(int(x/gcd(*fraction)) for x in fraction)
