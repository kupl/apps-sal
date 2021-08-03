def adjacent_element_product(arr):
    s = []
    for i in range(len(arr) - 1):
        s.append(arr[i] * arr[i + 1])
    n = max(s)
    return n
