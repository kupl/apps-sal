def sort_by_value_and_index(arr):
    return [e for (i, e) in sorted(enumerate(arr, 1), key=lambda t: t[0] * t[1])]
