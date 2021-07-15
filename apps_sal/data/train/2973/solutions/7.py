def array_conversion(arr):
    ops = [int.__mul__, int.__add__]
    c = 1
    while len(arr) != 1:
        arr = [ops[c](x, y) for x, y in zip(arr[::2], arr[1::2])]
        c = 1 - c
    return arr[0]
