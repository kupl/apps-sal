from math import gcd


def parameter(n):
    total = sum(int(x) for x in str(n))
    product = 1
    for num in str(n):
        product *= int(num)
    return (total * product) // gcd(total, product)
