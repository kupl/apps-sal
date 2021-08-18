def gimme(input_array):
    temp = input_array[:]
    temp.sort()
    middle_value = int(len(input_array)) // 2
    return input_array.index(temp[middle_value])
