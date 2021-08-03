def hello(name=""):
    if name != "":
        name = name.capitalize()
        return ("Hello, %s!" % name)
    else:
        return "Hello, World!"
    pass
