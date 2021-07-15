def sum_array(arr):
    if not arr:
        return 0
    arr.remove(max(arr))
    if not arr:
        return 0
    arr.remove(min(arr))
    return sum(arr)
