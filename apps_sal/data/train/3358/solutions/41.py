def correct(string):
    string = string.replace('1', 'I')
    string = string.replace('0', 'O')
    return string.replace('5', 'S')
