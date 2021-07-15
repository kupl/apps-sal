from typing import Optional

def hello(*args) -> str:
    """ Get "Hello, ${name}!" to a given name, or says "Hello, World!" if name is not given. """
    if args and len(args[0]):
        name = args[0]
    else:
        name = "world"
    return "Hello, {}!".format(name.title())
