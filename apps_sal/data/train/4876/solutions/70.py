def hello(name = None):
    if name == None or len(name) < 1: return "Hello, World!"
    return f"Hello, {name.capitalize()}!"
