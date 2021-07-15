def correct(string):
    output = ""
    for letter in string:
        if letter == '5':
            output += 'S'
        elif letter == '0':
            output += 'O'
        elif letter == '1':
            output += 'I'
        else:
            output += letter
    return output
