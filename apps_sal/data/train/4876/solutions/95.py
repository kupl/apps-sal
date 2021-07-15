def hello(name = ""):
    n = name.lower().capitalize()
    if len(name) == 0:
        return "Hello, World!"
    else:
        return "Hello, {}!".format(n)
