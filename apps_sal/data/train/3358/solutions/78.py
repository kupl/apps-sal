def correct(string):
    for element in string:
        string = string.replace('1', 'I')
        string = string.replace('5', 'S')
        string = string.replace('0', 'O')
    return string
