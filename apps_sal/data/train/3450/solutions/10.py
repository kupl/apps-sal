def array(string):
    s = string.replace(" ", "").split(",")
    return " ".join(s[1:-1]) if len(s) > 2 else None
