def minimum(arr):
    low = arr[0]
    for i in arr:
        if i < low:
            low = i
    return low

def maximum(arr):
    high= arr[0]
    for i in arr:
        if i > high:
            high = i
    return high
