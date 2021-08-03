def hello(name=False):
    if name:
        return "Hello, " + name.capitalize() + "!"
    else:
        return "Hello, World!"
