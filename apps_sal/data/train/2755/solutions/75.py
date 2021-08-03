def multiple_of_index(arr):
    newA = []
    for i in range(1, len(arr)):
        if arr[i] % i == 0:
            newA.append(arr[i])
    return newA
