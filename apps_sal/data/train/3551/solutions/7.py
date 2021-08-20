def array_previous_less(arr):
    return [next((v1 for v1 in arr[:i][::-1] if v1 < v), -1) for (i, v) in enumerate(arr)]
