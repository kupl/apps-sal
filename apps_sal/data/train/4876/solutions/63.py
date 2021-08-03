def hello(name=''):
    if name == "" or name == None:
        return "Hello, World!"
    else:
        name1 = name.lower()
        name2 = name1.capitalize()
        return f"Hello, {name2}!"
