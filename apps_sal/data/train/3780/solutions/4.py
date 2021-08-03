def example_sort(arr, example_arr):
    empty = []
    for i in example_arr:
        if i in arr:
            empty.extend([i] * arr.count(i))

    return empty
