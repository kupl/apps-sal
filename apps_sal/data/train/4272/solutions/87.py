def greet(name):
    greeting = 'Hello, {name}!'.format(name=name)
    if name == 'Johnny':
        return 'Hello, my love!'
    else:
        return greeting
