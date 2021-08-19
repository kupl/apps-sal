def array_change(arr):
    if not arr:
        return 0
    (x, y) = (arr[0], 0)
    for i in arr[1:]:
        x = max(x + 1, i)
        y += x - i
    return y
