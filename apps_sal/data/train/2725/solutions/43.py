def gimme(input_array):
    maximum = max(input_array)
    minimum = min(input_array)
    for i in input_array:
        if i != maximum and i != minimum:
            mean = input_array.index(i)
    return mean
