from operator import add, mul

def array_conversion(arr):
    iteration = 0
    while len(arr) > 1:
        iteration += 1
        arr = [(add if iteration & 1 else mul)(a, b) for a, b in zip(arr[::2], arr[1::2])]
    return arr[0]
