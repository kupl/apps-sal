def greet(name, owner):
    string = ''
    if name == owner:
        string += 'boss'
    else:
        string += 'guest'
    return 'Hello ' + string
