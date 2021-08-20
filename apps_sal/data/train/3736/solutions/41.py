def minimum(arr):
    min = float('inf')
    for x in arr:
        if x < min:
            min = x
    return min


def maximum(arr):
    max = float('-inf')
    for x in arr:
        if x > max:
            max = x
    return max
