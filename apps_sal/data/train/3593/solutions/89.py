def capitalize(s, ind):
    s = list(s)
    for e in ind:
        try:
            s[e] = s[e].capitalize()
        except:
            continue
    return ''.join(s)
