def find_longest(arr):
    return int(max(map(str, arr), key=len))
