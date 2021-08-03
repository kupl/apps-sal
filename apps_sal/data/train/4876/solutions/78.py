def hello(name=''):
    if name == '':
        return 'Hello, World!'
    else:
        name = name = ''.join(w[0].upper() + w[1:].lower() for w in name.split())
        return f'Hello, {name}!'
