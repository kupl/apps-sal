def say_hello(name, city, state):
    name = ' '.join(part for part in name)
    return f'Hello, { name }! Welcome to {city}, {state}!'
