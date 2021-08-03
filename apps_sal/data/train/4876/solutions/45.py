def hello(name=""):
    name = name.lower()
    name = name.title()
    if name != "":
        return f"Hello, {name}!"
    else:
        return f"Hello, World!"
