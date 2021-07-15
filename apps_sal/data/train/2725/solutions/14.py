def gimme(input_array):
    a = input_array.copy()
    a.sort()
    b = a[1]
    return input_array.index(b)
