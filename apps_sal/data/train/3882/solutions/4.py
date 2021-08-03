def sort_by_value_and_index(arr):
    return [elem[1] for elem in sorted(enumerate(arr, 1), key=lambda elem: elem[0] * elem[1])]
