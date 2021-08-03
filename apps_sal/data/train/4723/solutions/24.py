def greet(name):
    x = name.lower()
    t = x[1:len(name)]
    s = x[0].upper()
    return "Hello " + s + t + "!"
