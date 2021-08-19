def say_hello(name, city, state):
    full = name[0]
    for x in range(len(name) - 1):
        full = full + ' ' + name[x + 1]
    return f'Hello, {full}! Welcome to {city}, {state}!'
