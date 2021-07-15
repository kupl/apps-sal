def gimme(input_array):
    return input_array.index(list(set(input_array) - {min(input_array)} - {max(input_array)})[0])

