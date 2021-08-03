def multiple_of_index(arr):
    mult = []
    for i in range(1, len(arr)):
        if arr[i] % i == 0:
            mult.append(arr[i])
    return mult
