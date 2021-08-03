def hello(name=0):
    return "Hello, World!" if not name else "Hello, {}!".format(name.capitalize())
