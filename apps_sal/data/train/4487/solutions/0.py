def order_type(arr):
    if not arr:
        return 'Constant'
    arr = list(map(len, [str(elt) if type(elt) == int else elt for elt in arr]))
    cmp = sorted(arr)
    if arr == [arr[0]] * len(arr):
        s = 'Constant'
    elif arr == cmp:
        s = 'Increasing'
    elif arr == cmp[::-1]:
        s = 'Decreasing'
    else:
        s = 'Unsorted'
    return s
