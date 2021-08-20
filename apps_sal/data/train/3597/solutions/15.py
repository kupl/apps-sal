def say_hello(name, city, state):
    names = ''
    for i in name:
        names += i + ' '
    names = names.rstrip()
    return 'Hello, {names}! Welcome to {city}, {state}!'.format(names=names, city=city, state=state)
