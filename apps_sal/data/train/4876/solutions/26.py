def hello(name='World'):
    if len(name) == 0:
        return 'Hello, World!'
    else:
        return 'Hello, ' + name.title() + '!'
