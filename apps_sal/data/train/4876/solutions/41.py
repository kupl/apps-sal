def hello(name=''):
    if len(name) == 0:
        name = 'World'
    return 'Hello, ' + str(name.lower()).capitalize() + '!'
