def say_hello(name, city, state):
    n = ""    
    for el in name:
        n += " " + el
    return f'Hello,{n}! Welcome to {city}, {state}!'
