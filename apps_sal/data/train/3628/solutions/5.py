def rotate(arr, n):
    new_arr = arr[:]
    for idx in range(len(arr)):
        new_idx = (idx + n) % len(arr)
        new_arr[new_idx] = arr[idx]
    return new_arr
