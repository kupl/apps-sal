from math import log2


def array_conversion(arr):
    for it in range(int(log2(len(arr)))):
        arr = [arr[i] * arr[i + 1] if it % 2 else arr[i] + arr[i + 1] for i in range(0, len(arr), 2)]
    return arr[0]
