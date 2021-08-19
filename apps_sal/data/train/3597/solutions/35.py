def say_hello(name, city, state):
    c = ''
    for x in name:
        c = c + x + ' '
    c = c.rstrip(' ')
    return 'Hello, ' + c + '! Welcome to ' + city + ', ' + state + '!'
