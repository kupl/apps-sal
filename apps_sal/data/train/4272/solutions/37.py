def greet(name):
    greet = 'Hello, {name}!'.format(name=name)
    if name == 'Johnny':
        greet = 'Hello, my love!'
    else:
        greet = 'Hello, {name}!'.format(name=name)
    return greet
