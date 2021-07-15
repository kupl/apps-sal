def hello(name=''):
    return 'Hello, World!' if name is None or name == '' else f'Hello, {name.capitalize()}!'
