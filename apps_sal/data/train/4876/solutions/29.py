def hello(name='World'):
    if name == '':
        name = 'World'

    def toLower(x):
        return x.lower() if len(x) > 0 else ''
    return 'Hello, ' + name[0].upper() + toLower(name[1:]) + '!'
