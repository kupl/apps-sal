def scramble(string, array):
    return ''.join((v for (_, v) in sorted(zip(array, string))))
