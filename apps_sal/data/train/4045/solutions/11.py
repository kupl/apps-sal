def number(lines):
    i = 1
    l = []
    for item in lines:
        l.append((str(i) + ": " + item))
        i += 1
    return l
