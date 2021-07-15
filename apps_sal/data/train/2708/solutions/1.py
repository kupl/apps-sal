def yes_no(arr):
    result = []
    while arr:
        result.append(arr.pop(0))
        if arr:
            arr.append(arr.pop(0))
    return result
