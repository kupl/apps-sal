def capitalize(s, arr):
    s = list(s)
    for i in arr:
        try:
            s[i] = s[i].upper()
        except IndexError:
            continue
    return "".join(s)
