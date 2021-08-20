def greet(name):
    if name == 'Johnny':
        x = 'Hello, my love!'
    else:
        x = 'Hello, {name}!'.format(name=name)
    return x
