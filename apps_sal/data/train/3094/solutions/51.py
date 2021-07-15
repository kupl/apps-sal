def sum_array(arr = 0):
    if arr == None:
        return 0
    return sum(arr) - min(arr) - max(arr) if len(arr) >= 3 else 0
