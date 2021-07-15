def sum_two_smallest_numbers(num_array):
    smallest1 = min(num_array)
    index_smallest1 = num_array.index(smallest1)
    smallest2 = max(num_array)
    length_array = num_array.__len__()
    index = 0
    while index < length_array:
        if not index == index_smallest1 and num_array[index] <= smallest2:
            smallest2 = num_array[index]
        index += 1
    return smallest1 + smallest2
