def hello(name='World'):
    if name == '':
        return 'Hello, World!'
    return 'Hello, {}!'.format(name[:1].upper() + name[1:].lower())
