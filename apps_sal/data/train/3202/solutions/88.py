def greet(name, owner):
    name = "boss" if name == owner else "guest"
    return "Hello " + name
