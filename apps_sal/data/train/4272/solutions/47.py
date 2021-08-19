def greet(name):
    if name == 'Johnny':
        return 'Hello, my love!'.format(name=name)
    else:
        return f'Hello, {name}!'.format(name=name)
