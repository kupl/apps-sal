def minimum(arr):
    min = arr[0]
    for i in arr[1:]:
        if min > i:
            min = i
    return min

def maximum(arr):
    max = arr[0]
    for i in arr[1:]:
        if max < i:
            max = i
    return max
