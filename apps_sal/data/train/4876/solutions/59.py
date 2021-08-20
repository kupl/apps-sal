def hello(*name):
    if name == ():
        return 'Hello, World!'
    elif name[0] == '':
        return 'Hello, World!'
    else:
        return 'Hello, ' + name[0].lower().capitalize() + '!'
