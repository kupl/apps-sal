def hello(name=None):
    if name == '' or name == None:
        return "Hello, World!"
    else:
        name = name.lower()
        name = name.capitalize()

        return "Hello, " + name + "!"
