def minimum(arr):
    val = arr[0]
    for i in arr:
        if i < val:
            val = i
    return val


def maximum(arr):
    val = arr[0]
    for i in arr:
        if i > val:
            val = i
    return val
