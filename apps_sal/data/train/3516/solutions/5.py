def present(x, y):
    if x == "badpresent":
        return "Take this back!"
    if x == "goodpresent":
        return "".join([chr(ord(el) + y) for el in x])
    if x == "crap" or x == "empty":
        return "".join(sorted(x))
    if x == "bang":
        return str(sum([ord(el) - y for el in x]))
    if x == "dog":
        return f'pass out from excitement {y} times'
