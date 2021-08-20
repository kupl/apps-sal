import math


def getNumber(n):
    N = n
    number = ''
    divisor = 9
    while divisor > 1 and n > 0:
        if n % divisor == 0:
            number += str(divisor)
            n //= divisor
        else:
            divisor -= 1
    return int(number[::-1]) if number and n == 1 else -1


def digits_product(product):
    if product == 0:
        return 10
    if 0 < product < 10:
        return 10 + product
    return getNumber(product)
