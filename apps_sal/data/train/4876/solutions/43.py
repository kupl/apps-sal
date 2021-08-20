def hello(name=''):
    if name:
        name = name.lower().capitalize()
        return 'Hello, {}!'.format(name)
    else:
        return 'Hello, World!'
