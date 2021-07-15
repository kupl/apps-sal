from math import sqrt
from functools import reduce

CACHE = {}

def get_divisors_gen(number):
    if number in CACHE:
        return CACHE[number]
    
    divisors = []
    for i in range(1, int(number / 2) + 1):
        if number % i == 0:
            divisors.append(i)
    divisors.append(number)

    CACHE[number] = divisors
    
    return divisors
    

def list_squared(m, n):
    result = []
    for number in range(m, n+1):
        div_sq_sum = reduce(
            lambda acc, item: acc + item**2,
            get_divisors_gen(number)
        )
        if sqrt(div_sq_sum).is_integer():
            result.append([number, div_sq_sum])
    return result
