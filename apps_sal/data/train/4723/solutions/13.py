def greet(name):
    name = name.lower()
    return 'Hello {}!'.format(name.replace(name[0], name[0].upper(), 1))
