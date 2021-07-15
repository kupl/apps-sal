from fractions import gcd
def sum_differences_between_products_and_LCMs(pairs):
    return sum(x * (y - y / (gcd(x, y) or 1)) for x, y in pairs)

