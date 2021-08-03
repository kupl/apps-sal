def correct(string):
    string2 = ''
    for char in string:
        if char == '0':
            string2 = string2 + 'O'
        elif char == '1':
            string2 = string2 + 'I'
        elif char == '5':
            string2 = string2 + 'S'
        else:
            string2 = string2 + char
    return string2
