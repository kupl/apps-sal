def capitalize(s, ind):
    new = list(s)
    for i in ind:
        if i > len(s):
            pass
        else:
            new[i] = new[i].upper()
    return ''.join(new)
