def minimum(arr):
    min_value = arr[0]
    for num in arr:
        if num < min_value:
            min_value = num
    return min_value


def maximum(arr):
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value
