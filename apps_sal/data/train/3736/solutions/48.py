def minimum(arr):
    minv = 10e7
    for i in range(len(arr)):
        if arr[i] < minv:
            minv = arr[i]
    return minv

def maximum(arr):
    maxv = -10e7
    for i in range(len(arr)):
        if arr[i] > maxv:
            maxv = arr[i]
    return maxv
