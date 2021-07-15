def sort_by_value_and_index(arr):
    arr = zip(range(1, len(arr) + 1), arr)
    return [x[1] for x in sorted(arr, key=lambda x: x[0] * x[1])]
