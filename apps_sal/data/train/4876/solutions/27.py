def hello(name = ''):
    if not name:
        return 'Hello, World!'
    return f'Hello, {name[0].upper()}{name[1:].lower()}!'
