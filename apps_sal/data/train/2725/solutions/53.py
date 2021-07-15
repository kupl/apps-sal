def gimme(input_array):
    # Implement this function
    orig = input_array[:]
    input_array.sort()
    middle = int((len(input_array) - 1) / 2)
    return orig.index(input_array[middle])
