def scramble(string, array):
    d = dict(list(zip(array, string)))
    return ''.join(map(d.get, list(range(len(array)))))
