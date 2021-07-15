def hello(name = None):
    if name:
        capName = name.capitalize()
        if capName:
            return "Hello, {}!" .format(capName)
        else:
            return "Hello, World!" 
    else:
        return "Hello, World!" 
