def capitalize(s):
    x = "".join([i[1] if i[0] % 2 == 0 else i[1].upper() for i in enumerate(s)])
    y = "".join([i[1].upper() if i[0] % 2 == 0 else i[1] for i in enumerate(s)])
    return [y, x]
