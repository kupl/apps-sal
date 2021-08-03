def scramble(string, array):
    return "".join([string[array.index(i)] for i in range(len(array))])
