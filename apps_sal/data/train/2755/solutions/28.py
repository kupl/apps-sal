def multiple_of_index(arr):
    oplst = []

    for i in range(1, len(arr)):
        if arr[i] % i == 0:
            oplst.append(arr[i])

    return oplst
