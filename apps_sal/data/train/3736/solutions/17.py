def minimum(arr):
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
    return arr[0]


def maximum(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr[len(arr) - 1]
