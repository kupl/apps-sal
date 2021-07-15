def hello(name = "World"):
    if not name:
        name = "World"
    return "Hello, " + name.lower().capitalize() + "!"
