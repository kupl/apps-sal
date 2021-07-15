def gimme(input_array):
    for number in input_array:
        if number != max(input_array) and number != min(input_array):
            answer = number
    return input_array.index(answer)

