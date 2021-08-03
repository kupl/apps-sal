def hello(name=None):
    return "Hello, World!" if name in ["", None] else "Hello, {}!".format(name.capitalize())
