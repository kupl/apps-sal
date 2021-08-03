def scramble(string, array):
    return ''.join(v for i, v in sorted(zip(array, string)))
