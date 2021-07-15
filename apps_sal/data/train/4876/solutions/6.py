def hello(name='World'):
    return 'Hello, {}!'.format(name.capitalize() if name else 'World')
