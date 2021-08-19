def number(lines):
    ls = []
    for (i, l) in enumerate(lines):
        ls.append(str(i + 1) + ': ' + l)
    return ls
