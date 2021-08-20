def binary_array_to_number(arr):
    return sum((item * 2 ** index for (index, item) in enumerate(reversed(arr))))
