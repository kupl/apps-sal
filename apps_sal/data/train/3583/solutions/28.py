def binary_array_to_number(arr):
    arr = ("".join([str(x) for x in arr]))
    return int(arr, 2)
