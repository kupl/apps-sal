def sum_array(arr):
    if arr and len(arr) == 1:
        return 0
    elif arr: 
        return sum(arr) - (max(arr) + min(arr))
    else:
        return 0
