def find_dup(arr):
    return sum(arr) - sum(range(1, max(arr)+1))
