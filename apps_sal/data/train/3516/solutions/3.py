def present(x, y):
    if x == "goodpresent":
        return "".join(chr(ord(c) + y) for c in x)
    elif x in {"crap", "empty"}:
        return "".join(sorted(x))
    elif x == "bang":
        return str(sum(ord(c) - y for c in x))
    elif x == "badpresent":
        return "Take this back!"
    elif x == "dog":
        return f"pass out from excitement {y} times"
