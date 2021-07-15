def adjacent_element_product(arr):
    return sorted([arr[x] * arr[x + 1] for x in range(len(arr) -1 )] , reverse=True)[0]

