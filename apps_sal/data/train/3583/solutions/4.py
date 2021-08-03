def binary_array_to_number(arr):
    return sum(2**i for i, n in enumerate(arr[::-1]) if n)
