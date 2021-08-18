def gimme(input_array):

    for pos, num in enumerate(input_array):
        if num != min(input_array) and num != max(input_array):
            return pos
