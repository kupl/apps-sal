from operator import mul
from functools import reduce

def product_array(numbers):
    tot = reduce(mul,numbers)
    return [tot//n for n in numbers]
