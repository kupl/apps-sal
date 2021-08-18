def gimme(input_array):
    orig = input_array[:]
    input_array.sort()
    middle = int((len(input_array) - 1) / 2)
    return orig.index(input_array[middle])
