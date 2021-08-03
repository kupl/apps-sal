def capitalize(s):
    alternate = "".join(x.lower() if c % 2 == 1 else x.upper() for c, x in enumerate(s))
    return [alternate, alternate.swapcase()]
