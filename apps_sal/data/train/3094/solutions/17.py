def sum_array(arr):
    if arr is None or len(arr) < 2:
        return 0
    lowest = min(arr)
    highest = max(arr)
    sum = 0
    for x in arr:
        sum += x
    return sum - lowest - highest
