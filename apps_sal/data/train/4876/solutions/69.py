def hello(name=None):
    if name == None:
        return 'Hello, World!'
    elif name == '':
        return 'Hello, World!'
    else:
        name = name.capitalize()
        return 'Hello, ' + name + '!'

