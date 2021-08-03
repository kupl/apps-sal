def pairs(arr):
    return sum(abs(a - b) == 1 for a, b in zip(arr[::2], arr[1::2]))
