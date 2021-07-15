def capitalize(s,ind):
    new_s = ''
    for i, c in enumerate(s):
        if i in ind:
            new_s = new_s + c.upper()
        else:
            new_s = new_s + c
    return new_s
