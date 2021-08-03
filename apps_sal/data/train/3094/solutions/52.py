def sum_array(arr):
    if arr == None:
        return 0
    elif len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return 0
    else:
        arr.remove(max(arr))
        arr.remove(min(arr))
        return sum(arr)
