def correct(string):
    dic1 = {'5': 'S', '0': 'O', '1': 'I'}
    return ''.join((dic1.get(char, char) for char in string))
