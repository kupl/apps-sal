from copy import copy


def gimme(input_array):
    g = copy(input_array)
    g.sort()
    return input_array.index(g[1])
