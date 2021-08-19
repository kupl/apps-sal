def find_smallest_int(arr):
    minVal = float('inf')
    for i in arr:
        if i < minVal:
            minVal = i
    return minVal
