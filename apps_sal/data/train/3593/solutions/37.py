def capitalize(s, ind):  # jai shree ram!!!!
    for i in ind:
        if i < len(s):
            s = s[:i] + s[i].upper() + s[i + 1:]
    return s
