def gimme(input_array):
    middle_idx = len(input_array) // 2
    middle_value = sorted(input_array)[middle_idx]
    return input_array.index(middle_value)

