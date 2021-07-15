def greet(name):
    name =name.format(name=name)
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, " + str(name)+"!"
