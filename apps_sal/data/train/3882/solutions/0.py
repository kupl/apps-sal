def sort_by_value_and_index(arr):
    return [y[1] for y in sorted(enumerate(arr), key=lambda x:(x[0] + 1) * x[1])]
