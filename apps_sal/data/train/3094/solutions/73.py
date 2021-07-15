def sum_array(arr):
    if arr is None or len(arr) <= 1:
        return 0    
    return sum(arr) - (max(arr) + min(arr))
