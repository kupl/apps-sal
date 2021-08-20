def say_hello(name, city, state):
    real_name = ''
    for n in name:
        real_name += n + ' '
    return 'Hello, {0}! Welcome to {1}, {2}!'.format(real_name[:-1], city, state)
