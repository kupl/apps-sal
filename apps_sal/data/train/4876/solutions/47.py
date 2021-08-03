def hello(name="World"):
    if not name:
        return("Hello, World!")
    else:
        return("Hello, " + name.capitalize() + "!")


hello()

hello("John")

hello("aLIce")

hello("")

hello('')
