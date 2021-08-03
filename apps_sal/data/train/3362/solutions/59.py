def sum_mix(arr):
    for i, el in enumerate(arr):
        if isinstance(el, str):
            arr[i] = int(el)
    return sum(arr)
