def multiple_of_index(arr):
    result = list()
    for i in range(1, len(arr)):
        if(arr[i] % i == 0):
            result.append(arr[i])
    return result
