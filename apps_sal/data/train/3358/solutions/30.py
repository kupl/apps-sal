def correct(string):
    matches = '501'
    for char in string:
        if char in matches:
            if char == '5':
                string = string.replace(char, 'S')
            if char == '0':
                string = string.replace(char, 'O')
            if char == '1':
                string = string.replace(char, 'I')
    return string
