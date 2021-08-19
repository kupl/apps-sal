def hello(name="World"):
    # check if we passed empty string ''
    if len(name) == 0:
        return "Hello, World!"
    else:
        new_name = name[0].upper() + name[1:].lower()
        return "Hello, " + new_name + "!"
