def adjacent_element_product(arr):
    return max(arr[i] * n for i, n in enumerate(arr[1:]))
