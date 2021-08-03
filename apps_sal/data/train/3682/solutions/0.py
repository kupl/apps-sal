def string_constructing(a, s):
    if len(s) == 0:
        return 0
    i = -1
    for j, c in enumerate(s):
        i = a.find(c, i + 1)
        if i < 0 or i == len(a) - 1:
            break
    return len(a) - j + (i < 0) + string_constructing(a, s[j + (i >= 0):])
