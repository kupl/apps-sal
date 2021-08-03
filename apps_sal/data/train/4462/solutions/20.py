def adjacent_element_product(arr):
    a = arr[0] * arr[1]
    for i in range(1, len(arr)):
        if arr[i] * arr[i - 1] > a:
            a = arr[i] * arr[i - 1]
    return a
