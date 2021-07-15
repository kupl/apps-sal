def hello(name="World"):
    return "Hello, %s!" % (name.lower().capitalize() if name != "" else "World")
