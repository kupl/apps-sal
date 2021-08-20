def find_dup(arr):
    return sum(arr) - len(arr) * (len(arr) - 1) / 2
