def min_sum(arr):
    # Your code here
    s = 0
    arr = sorted(arr)
    while arr:
        s = s + arr.pop(0)*arr.pop(-1)
    return s
