def multiple_of_index(arr):
    result = []
    for i in range(len(arr)):
        if i != 0:
            if arr[i] % i == 0:
                result.append(arr[i])
    return result
