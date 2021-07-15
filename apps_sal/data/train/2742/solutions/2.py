def scramble(string, lst):
    result = [None] * len(string)
    for char, index in zip(string, lst):
        result[index] = char
    return "".join(result)
