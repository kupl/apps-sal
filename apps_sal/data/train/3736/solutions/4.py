def minimum(arr):
    min_ = arr[0]
    for e in arr[1:]:
        if e < min_:
            min_ = e
    return min_


def maximum(arr):
    max_ = arr[0]
    for e in arr[1:]:
        if e > max_:
            max_ = e
    return max_
