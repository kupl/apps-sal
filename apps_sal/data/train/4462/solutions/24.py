def adjacent_element_product(array):
    john = []
    for i, v in enumerate(array):
        if i == len(array) - 1:
            pass
        else:
            john.append(array[i] * array[i + 1])
    return max(john)
