def gimme(input_array):
    for x in range(len(input_array)):
        if min(input_array) != input_array[x] and max(input_array) != input_array[x]:
            return x
