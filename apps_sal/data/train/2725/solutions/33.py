def gimme(input_array):
    minimum = min(input_array)
    maximum = max(input_array)
    for l in input_array:
        if l < maximum and l > minimum:
            return input_array.index(l) 

