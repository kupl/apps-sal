def gimme(input_array):
    for i in input_array:
        if i < input_array[-1] and i > input_array[0]:
            return input_array.index(i)
        elif i < input_array[0] and i > input_array[-1]:
            return input_array.index(i)
        elif i < input_array[1] and i > input_array[0]:
            return input_array.index(i)
        elif i < input_array[0] and i > input_array[1]:
            return input_array.index(i)
        elif i < input_array[1] and i > input_array[-1]:
            return input_array.index(i)
        elif i < input_array[-1] and i > input_array[1]:
            return input_array.index(i)
