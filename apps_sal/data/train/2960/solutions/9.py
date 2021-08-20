from math import gcd


def sum_differences_between_products_and_LCMs(pairs):

    def lcm(x, y):
        return x * y // gcd(x, y) if x and y else 0
    return sum((x * y - lcm(x, y) for [x, y] in pairs))
