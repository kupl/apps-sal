def greet(name, owner):
    if name == owner:
        return "Hello boss"
    elif name != owner:
        return "Hello guest"
    else:
        return 0
