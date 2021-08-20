def say_hello(name, city, state):
    x = ''
    for i in name:
        x += i + ' '
    y = x.strip()
    return 'Hello, {}! Welcome to {}, {}!'.format(y, city, state)
