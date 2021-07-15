def string_clean(s):
    new=""
    for char in s:
        if char in "1234567890":
            new+=""
        else: new+=char
    return new

