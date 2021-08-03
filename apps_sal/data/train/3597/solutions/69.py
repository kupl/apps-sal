def say_hello(name, city, state):
    n = ""
    for i in name:
        n = n + " " + i
    txt = "Hello," + n + "! Welcome to {}, {}!"
    return txt.format(city, state)
