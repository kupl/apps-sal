def total(arr):
    if len(arr) == 1:
        return arr[0]
    arr2 = []
    for i in range(len(arr) - 1):
        arr2.append(arr[i] + arr[i + 1])
    return total(arr2)
