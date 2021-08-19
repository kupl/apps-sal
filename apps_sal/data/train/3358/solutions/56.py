def correct(string):
    a = [('0', 'O'), ('5', 'S'), ('1', 'I')]
    for (x, y) in a:
        string = string.replace(x, y)
    return string
