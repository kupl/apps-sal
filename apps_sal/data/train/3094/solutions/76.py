def sum_array(arr):
    if arr and len(arr)>2:
        arr.pop(arr.index(max(arr)))
        arr.pop(arr.index(min(arr)))
    else:
        return 0
    return sum(arr)

