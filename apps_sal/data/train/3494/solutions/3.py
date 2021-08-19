def pig_it(text):
    new_string = ''
    for each in text.split():
        if each == '?':
            new_string += '? '
        elif each == '!':
            new_string += '! '
        else:
            new_string += each[1:len(each)] + each[0] + 'ay '
    a = len(new_string)
    return new_string[0:a - 1]
