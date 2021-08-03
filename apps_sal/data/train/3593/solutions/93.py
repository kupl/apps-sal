def capitalize(s, ind):
    z = list(s)
    for i in ind:
        if i < len(s):
            z[i] = z[i].upper()
    return "".join(z)
