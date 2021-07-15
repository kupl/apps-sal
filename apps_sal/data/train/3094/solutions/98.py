def sum_array(arr):
    if arr == None or len(arr) <= 2:
        return 0
    else:
        return sum([x for x in arr]) - min(arr) - max(arr)
