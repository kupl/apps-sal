def nerdify(txt):
    encoder = {'a': '4', 'A': '4', 'e': '3', 'E': '3', 'l': '1'}
    return ''.join(encoder.get(c, c) for c in txt)

