def accum(s):
    value = ""
    for i, c in enumerate(s):
        value += c.upper() + c.lower() * i + "-"
    return value[:-1]
