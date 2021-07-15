def say_hello(name, city, state):
    string = ' '
    string1 = string.join(name)
    return "Hello, {string1}! Welcome to {city}, {state}!".format(string1=string1, city=city, state=state)
