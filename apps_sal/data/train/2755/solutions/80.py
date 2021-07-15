def multiple_of_index(arr):
    index = 1
    res = []
    while index < len(arr):
        if arr[index] % index == 0:
            res.append(arr[index])
        index += 1
    return res
