def minimum(arr: []):
    result = arr[0]
    for i in arr:
        if i < result:
            result = i
    return result


def maximum(arr: []):
    result = arr[0]
    for i in arr:
        if i > result:
            result = i
    return result
