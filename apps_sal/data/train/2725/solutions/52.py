def gimme(input_array):
    a = max(input_array)
    b = min(input_array)
    for i in input_array :
        if i == a or i == b:
            continue
        else :
            return input_array.index(i)
