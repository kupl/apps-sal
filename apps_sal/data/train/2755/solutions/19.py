def multiple_of_index(arr):
    ar = []
    for num in range(1, len(arr)):
        if arr[num] % num == 0:
            ar.append(arr[num])
    return ar
