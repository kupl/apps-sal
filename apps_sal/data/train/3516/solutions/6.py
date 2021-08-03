def present(x, y):
    if x == "empty":
        return "empty"
    if x == "crap":
        return "".join(sorted(x))
    if x == "badpresent":
        return "Take this back!"
    if x == "dog":
        return f"pass out from excitement {y} times"
    if x == "bang":
        return str(sum([ord(el) - y for el in x]))
    if x == "goodpresent":
        return "".join([chr(ord(el) + y)for el in x])
