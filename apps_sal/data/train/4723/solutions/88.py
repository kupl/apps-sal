def greet(name):
    name_lower = name.lower()
    name_final = name_lower[0].upper() + name_lower[1:]
    return "Hello " + name_final + "!"
