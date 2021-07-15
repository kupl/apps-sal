from fractions import gcd
def sum_differences_between_products_and_LCMs(pairs):
    return sum(i * j - (i * j // gcd(i, j)) for i, j in pairs if i and j)
