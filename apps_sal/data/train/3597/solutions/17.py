def say_hello(name, city, state):
    return 'Hello,' + (' {}' * len(name)).format(*name) + f'! Welcome to {city}, {state}!'
