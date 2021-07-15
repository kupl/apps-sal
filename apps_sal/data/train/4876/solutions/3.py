def hello(name=''):
    return "Hello, {}!".format(name.title() if name else 'World')
