def hello(name=None):
    name = name.capitalize() if name else "World"
    return "Hello, %s!"%(name)
