def greet(name, owner):
    # Add code here
    if name==owner:
        what = "boss"
    else:
        what = "guest"
    return "Hello {}".format(what)
