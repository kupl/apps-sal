def hello(name='world'):
    if name == '':
        name = 'world'
    return 'Hello, {}!'.format(name.title())
