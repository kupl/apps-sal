def correct(string):
    new_string = ''
    for letter in string:
        if letter == '5':
            new_string = new_string + 'S'
        elif letter == '1':
            new_string = new_string + 'I'
        elif letter == '0':
            new_string = new_string + 'O'
        else:
            new_string = new_string + letter
    return new_string
