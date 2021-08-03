d = {'a': '4', 'e': '3', 'l': '1', 'A': '4', 'E': '3'}


def nerdify(txt):
    return ''.join([d[i] if i in d else i for i in txt])
