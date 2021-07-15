def multiple_of_index(arr):
    return [x for x in [arr[i] if arr[i]%i == 0 else None for i in range(1, len(arr))] if x is not None]
