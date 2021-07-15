def number(lines):
    keks = []
    for index, i in enumerate(lines):
        keks.append(str(index + 1) + ": " + i)
    return keks
