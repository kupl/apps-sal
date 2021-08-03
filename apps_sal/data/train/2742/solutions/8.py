def scramble(string, array):
    return "".join(string[array.index(x)] for x in range(len(string)))
