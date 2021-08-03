def sort_by_value_and_index(arr):
    return [b for _, b in sorted(enumerate(arr, 1), key=lambda a: a[0] * a[1])]
