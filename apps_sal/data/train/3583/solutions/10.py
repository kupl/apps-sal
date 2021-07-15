from functools import reduce

def binary_array_to_number(a):
    return reduce(lambda t,b:t*2+b,a)
