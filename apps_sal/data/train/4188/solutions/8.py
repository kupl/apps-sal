def find_dup(arr):
    l = len(arr) - 1
    return sum(arr) - (l * (l + 1)) / 2
