def example_sort(arr, example_arr):
    d = {x: i for i, x in enumerate(example_arr)}
    return sorted(arr, key=d.__getitem__)

