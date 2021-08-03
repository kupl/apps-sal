def gimme(input_array):
    ord = sorted(input_array)[len(input_array) // 2]
    return input_array.index(ord)
