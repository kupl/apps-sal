def gimme(input_array):
    # Implement this function
    mins = min(input_array)
    maxs = max(input_array)
    for i in input_array:
        if i < maxs and i > mins:
            return input_array.index(i)
