def scramble(string, array):
    res = array[:]
    for (i, a) in enumerate(array):
        res[a] = string[i]
    return "".join(res)
