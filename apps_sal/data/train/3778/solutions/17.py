def find_smallest_int(arr):
    min = arr[0]
    for i in range(len(arr)):
        if i + 1 < len(arr):
            if arr[i + 1] < min:
                min = arr[i + 1]
    return min
