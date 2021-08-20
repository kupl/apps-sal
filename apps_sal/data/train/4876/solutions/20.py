import string


def hello(name='World'):
    if name == '':
        return 'Hello, World!'
    else:
        return 'Hello, ' + name.capitalize() + '!'
