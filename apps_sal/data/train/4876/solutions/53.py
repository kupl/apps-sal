def hello(name='World'):
    if name:
        return f'Hello, {name.lower().capitalize()}!'
    return 'Hello, World!'
