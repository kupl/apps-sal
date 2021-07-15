def sort_by_value_and_index(arr):
    return [b for _, b in sorted(enumerate(arr, 1), key=lambda x: int.__mul__(*x))]
