from functools import reduce


def binary_array_to_number(arr):
    def append_bit(n, b): return n << 1 | b
    return reduce(append_bit, arr)
