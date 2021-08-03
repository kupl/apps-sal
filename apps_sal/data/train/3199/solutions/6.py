def greet(name):
    if name == None:
        return None

    if len(name) > 0:
        return "hello " + name + "!"
    else:
        return None
