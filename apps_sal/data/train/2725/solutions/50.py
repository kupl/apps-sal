def gimme(input_array):
    newarr = input_array.copy()
    [newarr.remove(x) for x in [max(input_array), min(input_array)]]
    return input_array.index(newarr[0])
