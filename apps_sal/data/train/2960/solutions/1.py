from fractions import gcd


def lcm(x, y):
    return x * y / gcd(x, y) if gcd(x, y) else 0


def sum_differences_between_products_and_LCMs(pairs):
    return sum(x * y - lcm(x, y) for x, y in pairs)
