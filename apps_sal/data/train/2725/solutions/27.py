def gimme(input_array):
    for i, c in enumerate(input_array):
        if c == sorted(input_array)[1]:
            return i
