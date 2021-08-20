def min_sum(arr):
    arr = sorted(arr)
    n = 0
    while len(arr) > 0:
        x = arr.pop(0)
        y = arr.pop()
        n += x * y
    return n
