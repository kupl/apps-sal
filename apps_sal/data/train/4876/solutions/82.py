def hello(name=None):
    if name == None or name == '':
        return 'Hello, World!'
    else:
        name = name.lower()
        name = name.capitalize()
    return f'Hello, {name}!'
