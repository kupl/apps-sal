def hello(name=False):
    return 'Hello, {}!'.format(name.capitalize()) if name else 'Hello, World!'
