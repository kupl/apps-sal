def adjacent_element_product(arr):
    return len(arr) and max((x * y for (x, y) in zip(arr, arr[1:])))
