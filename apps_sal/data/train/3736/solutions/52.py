def minimum(arr):
    min = 1000000000
    for i in arr:
        if i < min:
            min = i
    return min


def maximum(arr):
    max = -1000000000
    for i in arr:
        if i > max:
            max = i
    return max
