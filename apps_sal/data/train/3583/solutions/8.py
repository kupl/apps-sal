def binary_array_to_number(arr):
    return int(bytearray(''.join((str(a) for a in arr)), encoding='utf-8'), base=2)
