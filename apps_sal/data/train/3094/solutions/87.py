def sum_array(arr):
    if arr:
        return sum(arr)-max(arr)-min(arr) if len(arr) > 1 else 0 
    else:
        return 0 
