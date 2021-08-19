def binary_array_to_number(arr, acc=0):
    if len(arr) == 0:
        return acc
    acc = acc << 1 | arr.pop(0)
    return binary_array_to_number(arr, acc)
