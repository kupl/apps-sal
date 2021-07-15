def gimme(input_array):
    print(input_array)
    middle = round(sum(input_array) - min(input_array) - max(input_array),2)
    index = input_array.index(middle)
    return index

