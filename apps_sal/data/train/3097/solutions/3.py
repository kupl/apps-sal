def rad_ladies(name):
    return "".join(c for c in name if c.isalpha() or c.isspace() or c == "!").upper()

