def hello(name = 'World'):
    if not name:
        return 'Hello, World!'
    else:
        return f'Hello, {name.capitalize()}!'

