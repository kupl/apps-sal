def gimme(input_array):
    max_num = max(input_array)
    min_num = min(input_array)

    for elem in input_array:
        if elem != max_num and elem != min_num:
            return input_array.index(elem)
