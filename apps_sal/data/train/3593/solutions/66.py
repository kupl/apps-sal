def capitalize(s,ind):
    s = list(s)
    for element in ind:
        if element <= len(s):
            s[element]=s[element].upper()
    return ''.join(s)
