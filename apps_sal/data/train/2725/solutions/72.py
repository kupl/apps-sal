def gimme(input_array):
    sort = sorted(input_array)
    x = sort[1]
    for i in range(len(input_array)):
        if x == input_array[i]:
            return i
