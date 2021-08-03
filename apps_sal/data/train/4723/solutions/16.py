def greet(name):
    first = name[0].upper()
    rest = name[1:len(name)].lower()
    return 'Hello ' + first + rest + '!'
