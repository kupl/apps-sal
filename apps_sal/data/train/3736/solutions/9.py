def minimum(arr):
    Min = arr[0]
    for e in arr:
        if e < Min:
            Min = e
    return Min


def maximum(arr):
    Max = arr[0]
    for e in arr:
        if e > Max:
            Max = e
    return Max
