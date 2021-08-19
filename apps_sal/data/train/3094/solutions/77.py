def sum_array(arr):
    if arr == None:
        return 0
    elif len(arr) <= 1:
        return 0
    else:
        return sum(arr) - (max(arr) + min(arr))
