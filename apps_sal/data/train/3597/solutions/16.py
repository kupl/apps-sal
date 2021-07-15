def say_hello(name, city, state):
    str_name = ""
    for i in name:
        str_name += i + " "
    str_name = str_name[:-1]
    return "Hello, {name}! Welcome to {city}, {state}!".format(name = str_name, city=city, state=state)
