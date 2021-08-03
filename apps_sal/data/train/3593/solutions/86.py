def capitalize(s, ind):
    j = list(s)
    for i in ind:
        if i < len(s) + 1:
            j[i] = j[i].upper()
    return "".join(j)
