def adjacent_element_product(array):
    arr = []
    left_index = 0
    right_index = -len(array) + 1
    middle_index = 1
    if len(array) == 2:
        return array[0] * array[1]
    while middle_index < len(array):
        arr.append(array[left_index] * array[right_index])
        left_index += 1
        right_index += 1
        middle_index += 1
    return max(arr)
