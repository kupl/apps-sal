def gimme(input_array):
    for e in input_array:
        i = 0
        for p in range(len(input_array)):
            if e > input_array[p]:
                i += 1
            if e < input_array[p]:
                i -= 1
        if i == 0:
            for ele in range(len(input_array)):
                if e == input_array[ele]:
                    return ele
