def greet(name):
    if name == 'Johnny':
        name = 'my love'
    else:
        name = name
    return 'Hello, {name}!'.format(name=name)
