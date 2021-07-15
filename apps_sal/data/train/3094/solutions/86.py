def sum_array(arr):
    if arr and len(arr) > 3:
        return sum(arr) - min(arr) - max(arr) 
    return 0
