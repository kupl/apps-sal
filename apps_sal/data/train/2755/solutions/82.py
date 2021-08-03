def multiple_of_index(arr):
    arr2 = []
    for i in range(len(arr)):
        if i > 0 and arr[i] % i == 0:
            arr2.append(arr[i])
    return arr2
    pass
