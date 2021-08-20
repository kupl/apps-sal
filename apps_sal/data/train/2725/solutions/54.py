def gimme(input_array):
    for x in input_array:
        if x != min(input_array) and x != max(input_array):
            choosen = x
    return input_array.index(choosen)
