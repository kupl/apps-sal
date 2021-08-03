
def hello(name=''):

    if name == None or name == '':
        return f'Hello, World!'
    else:
        name = name.lower()
        name = name.capitalize()
        return f'Hello, {name}!'
