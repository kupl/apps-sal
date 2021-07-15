def find_longest(arr):
    return int(max([str(n) for n in arr], key=len))
