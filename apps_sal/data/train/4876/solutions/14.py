def hello(name=''):
    if name:
        return f'Hello, {name[0].capitalize() + name[1:].lower()}!'
    else:
        return 'Hello, World!'
