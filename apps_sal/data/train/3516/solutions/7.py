def present(x,y):
    if x == '' or x == 'empty':
        return 'empty'
    elif x == 'crap':
        return 'acpr'
    elif x == 'badpresent':
        return 'Take this back!'
    elif x == 'dog':
        return 'pass out from excitement ' + str(y) + ' times'
    elif x == 'bang':
        output = 0
        for char in list(x):
            output += ord(char)-y
        return str(output)
    elif x == 'goodpresent':
        output = ''
        for char in list(x):
            output += chr(ord(char)+y)
        return output
    else:
        return 'lol'
