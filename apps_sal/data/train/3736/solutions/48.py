def minimum(arr):
    minv = 100000000.0
    for i in range(len(arr)):
        if arr[i] < minv:
            minv = arr[i]
    return minv


def maximum(arr):
    maxv = -100000000.0
    for i in range(len(arr)):
        if arr[i] > maxv:
            maxv = arr[i]
    return maxv
