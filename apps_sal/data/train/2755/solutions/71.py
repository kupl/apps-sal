def multiple_of_index(arr):
    returnArr = []
    for i in range(1, len(arr)):
        if arr[i] % i == 0:
            returnArr.append(arr[i])
    return returnArr
