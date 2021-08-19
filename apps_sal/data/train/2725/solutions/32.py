def gimme(input_array):
    # Implement this function
    temp = input_array[:]
    temp.sort()
    middle_value = int(len(input_array)) // 2
    return input_array.index(temp[middle_value])
