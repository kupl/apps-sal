def array(string):
    x = string.replace(" ", "").split(",")
    if len(x) < 3:
        return None
    return " ".join(x[1:-1])
