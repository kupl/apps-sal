def hello(name='World'):
    if name == '':
        name = 'World'
    name = list(name.lower())
    name[0] = name[0].upper()
    return 'Hello, {}!'.format(''.join(name))
