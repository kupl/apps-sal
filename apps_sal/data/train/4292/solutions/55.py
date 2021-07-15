def string_clean(s):
    c=""
    for i in s:
        if i not in "0123456789":
            c=c+i
    return c
