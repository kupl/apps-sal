def capitalize(s):
    x, y = "", ""
    for i, j in enumerate(s):
        if i % 2 == 0:
            x += j.upper()
            y += j.lower()
        else:
            y += j.upper()
            x += j.lower()
    return [x, y]
