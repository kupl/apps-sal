def hello(name=""):
    if name == "":
        name="World"
    name = name[0].upper() + name[1:].lower()
    return f"Hello, {name}!"
