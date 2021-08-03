def capitalize(s, ind):
    for i in ind:
        if i >= len(s):
            break
        s = s[:i] + s[i].capitalize() + s[i + 1:]
    return s
