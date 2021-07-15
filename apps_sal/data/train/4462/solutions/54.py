def adjacent_element_product(array):
    results_list = []
    prev = array[0]

    for element in array[1:]:
        maximum = prev * element
        prev = element
        results_list.append(maximum)

    return max(results_list)
