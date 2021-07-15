from functools import reduce
def binary_array_to_number(arr):
    append_bit = lambda n, b: n << 1 | b
    return reduce(append_bit, arr)

