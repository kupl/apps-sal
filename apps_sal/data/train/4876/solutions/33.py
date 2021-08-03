def hello(name=""):
    return "Hello, World!" if len(name) <= 0 else "Hello, " + name.lower().title() + "!"
