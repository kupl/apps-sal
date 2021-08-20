def hello(name='World'):
    if name == '':
        name = 'World'
    return 'Hello, {}!'.format(name.lower().capitalize())
