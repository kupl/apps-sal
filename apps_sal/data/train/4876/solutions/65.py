def hello(name=0):
    if name == "" or name == 0:
        return "Hello, World!"
    else:
        name = name.lower()
        name = name.capitalize()
        return "Hello, " + name + "!"
