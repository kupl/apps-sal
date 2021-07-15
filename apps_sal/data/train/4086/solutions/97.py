def first_non_consecutive(arr):
    x = arr[0]
    for index in arr:
        if index != x:
            result = index
            break
        x += 1
    else:
        result = None
    return result
