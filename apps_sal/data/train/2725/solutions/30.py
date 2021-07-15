def gimme(input_array):
    maxpos = input_array.index(max(input_array))
    minpos = input_array.index(min(input_array))
    for i in input_array:
        if input_array.index(i) != maxpos and input_array.index(i) != minpos:
            return input_array.index(i)
