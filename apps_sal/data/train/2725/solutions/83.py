def gimme(input_array):
    return input_array.index(sorted(input_array)[int((len(input_array) - 1) / 2)])
