def say_hello(name, city, state):
    element = ""
    for x in name:
        element = element + x + " "
    element = element[:-1]  
    return("Hello, "+element+"!"+" Welcome to "+city+", "+state+"!")
