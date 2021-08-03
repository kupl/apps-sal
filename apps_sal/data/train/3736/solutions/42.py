def minimum(arr):
    if len(arr) > 0:
        result = arr[0]
        if len(arr) > 1:
            for i in range(1, len(arr)):
                if arr[i] < result:
                    result = arr[i]
    else:
        result = 0
    return result


def maximum(arr):
    if len(arr) > 0:
        result = arr[0]
        if len(arr) > 1:
            for i in range(1, len(arr)):
                if arr[i] > result:
                    result = arr[i]
    else:
        result = 0
    return result
