def binary_array_to_number(arr):
    decimal = 0
    p = 0
    for x in reversed(arr):
        decimal += x * 2 ** p
        p += 1
    return decimal
