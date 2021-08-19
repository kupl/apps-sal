def greet(name):
    if name == '':
        return None
    elif isinstance(name, str):
        return 'hello ' + name + '!'
    else:
        return None
