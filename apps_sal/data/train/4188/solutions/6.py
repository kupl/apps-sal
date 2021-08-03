def find_dup(arr):
    return sum(arr, (1 - len(arr)) * len(arr) / 2)
