def say_hello(name, city, state):
    n = ""
    for i in range(len(name)):
        n = n + " " + name[i]

    return f'Hello, {n[1:]}! Welcome to {city}, {state}!'
