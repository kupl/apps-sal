def hello(name=None):
    if name:
        a = name.lower() 
        b = a.capitalize()
        return f"Hello, {b}!"
    elif not name:
        return "Hello, World!"
