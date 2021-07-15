def sum_array(arr):
    return sum(arr) - min(arr) - max(arr) if arr and len(arr) > 1 else 0
