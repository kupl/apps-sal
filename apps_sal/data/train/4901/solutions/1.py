from fractions import gcd


def lcm(a, b):
    return a * b / gcd(a, b)


def calculate_ratio(w, h):
    if all(x > 0 for x in [w, h]):
        return "{}:{}".format(lcm(w, h) / h, lcm(w, h) / w)
    return 'You threw an error'
