def minimum(arr):
    min = 9999999999999999999
    for i in arr:
        if(min > i):
            min = i
    return min


def maximum(arr):
    max = -9999999999999999999
    for i in arr:
        if(max < i):
            max = i
    return max
