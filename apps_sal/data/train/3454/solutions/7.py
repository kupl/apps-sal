import math


def lcm(x, y):
    return x * y // math.gcd(x, y)


def candies_to_buy(amount_of_kids_invited):
    f = 1
    for i in range(2, amount_of_kids_invited + 1):
        f = lcm(f, i)
    return f
