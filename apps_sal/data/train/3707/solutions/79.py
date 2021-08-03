def sorter(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j].lower() > arr[j + 1].lower():
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
