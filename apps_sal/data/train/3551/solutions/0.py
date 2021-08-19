def array_previous_less(arr):
    return [next((y for y in arr[:i][::-1] if y < x), -1) for (i, x) in enumerate(arr)]
