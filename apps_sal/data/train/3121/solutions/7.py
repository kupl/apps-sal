def solve(arr):
    special_set = set(arr)
    n = 0
    for i in list(special_set):
        n += i
    return n
