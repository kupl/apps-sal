def minimum(arr):
    Min = arr[0]
    for i in arr:
        if i < Min:
            Min = i
    return Min


def maximum(arr):
    Max = arr[0]
    for i in arr:
        if i > Max:
            Max = i
    return Max
