def hello(name="World"):
    if name == "":
        return "Hello, World!"

    else:
        return f"Hello, " + name.title() + "!"
