def multiple_of_index(arr):
    ar = []
    for i in range(1, len(arr)):
        if arr[i] % i == 0:
            ar.append(arr[i])
    return ar
