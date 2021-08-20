from functools import reduce
from operator import mul
PRODUCTS = {}
for n in range(10, 5000):
    dig_prod = reduce(mul, map(int, str(n)))
    if dig_prod < 600 and dig_prod not in PRODUCTS:
        PRODUCTS[dig_prod] = n


def digits_product(product):
    return PRODUCTS.get(product, -1)
