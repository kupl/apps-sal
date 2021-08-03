def gimme(input_array):
    x = max(input_array)
    y = min(input_array)

    for i in input_array:
        if i > y and i < x:
            return(input_array.index(i))
