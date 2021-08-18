def greet(name):
    name = name.lower()
    for i in name:
        o = name[0].upper() + name[1:]
    return f"Hello {o}!"
