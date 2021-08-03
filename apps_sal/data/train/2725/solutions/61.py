def gimme(input_array):
    x = sorted(list(input_array))
    for y in range(len(input_array)):
        if x[1] == input_array[y]:
            return y
