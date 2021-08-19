def gimme(input_array):
    middle_num = sorted(input_array)[1]
    counter = 0
    for i in input_array:
        if i == middle_num:
            return counter
        else:
            counter += 1


gimme([2, 3, 1])
