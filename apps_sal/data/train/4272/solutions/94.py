def greet(name):
    if name == 'Johnny':
        msg = 'Hello, my love!'
    else:
        msg = 'Hello, {name}!'.format(name=name)
    return msg
