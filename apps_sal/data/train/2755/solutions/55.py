def multiple_of_index(arr):
    result = []
    for i in range(1, len(arr)):
        if arr[i] % i == 0:
            result.append(arr[i])
        else:
            pass
    return result
