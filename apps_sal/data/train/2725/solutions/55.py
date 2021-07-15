def gimme(input_array):
    min_value = min(input_array)
    max_value = max(input_array)
    for idx, val in enumerate(input_array):
        if val == min_value:
            continue
        if val == max_value:
            continue
        return idx
