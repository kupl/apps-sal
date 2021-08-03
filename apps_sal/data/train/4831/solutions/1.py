def solved(string):
    b = str((len(string) - 1) / 2)
    b = int(b[:-2])
    if len(string) % 2 == 1:
        c = string[:b] + string[b + 1:]
        return ''.join(sorted(c))
    return ''.join(sorted(string))
