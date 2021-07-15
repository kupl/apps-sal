def unflatten(flat_array):
    arr = flat_array[:]
    for i, v in enumerate(arr):
        if v > 2:
            arr[i], arr[i+1:i+v] = arr[i:i+v], []
    return arr
