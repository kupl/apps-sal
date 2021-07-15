def say_hello(name, city, state):
    full_name = ''
    for n in name:
        full_name += n
        full_name += ' '
    return 'Hello, {}! Welcome to {}, {}!'.format(full_name[:-1], city, state)
