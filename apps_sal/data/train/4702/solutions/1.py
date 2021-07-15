from functools import reduce
from operator import mul

def digits_product(product):
    if product == 0:
        return 10
    elif len(str(product)) == 1:
        return int('1' + str(product))
    temp = product
    digits = []
    units = list(range(9, 1, -1))
    for i in units:
        if product % i == 0:
            exponent = 0
            while product % i == 0:
                exponent += 1
                product //= i
            digits.append((i, exponent))
    res = ""
    for digit, occurances in digits:
        res += str(digit)*occurances
    return int(res[::-1]) if res and reduce(mul, [int(i) for i in res]) == temp else -1
