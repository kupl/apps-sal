def min_sum(arr):
    arr.sort()
    s = 0
    while arr:
        s += arr.pop() * arr.pop(0)
    return s
