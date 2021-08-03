def yes_no(arr):
    result, i = [], 0
    while arr:
        result.extend(arr[i::2])
        j = i != len(arr) % 2
        arr = arr[1 - i::2]
        i = j
    return result
