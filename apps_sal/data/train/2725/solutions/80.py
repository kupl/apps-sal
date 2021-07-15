def gimme(input_array):
    inp2 = input_array.copy()
    inp2.remove(max(inp2))
    inp2.remove(min(inp2))
    return input_array.index(inp2[0])
