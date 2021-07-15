def gimme(input_array):
    a = []
    b = sum(input_array) / len(input_array)
    for i in input_array:
        a.append(abs(b-i))
    return a.index(min(a))

