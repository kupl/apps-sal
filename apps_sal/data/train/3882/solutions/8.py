def sort_by_value_and_index(arr):
    return [y for (x, y) in sorted(enumerate(arr, 1), key=lambda x: x[0] * x[1])]
