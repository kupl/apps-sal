def greet(name, owner):
    return f"Hello {name == owner and 'boss' or 'guest'}"
