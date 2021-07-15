def string_clean(s):
    a = ""
    for el in s:
        if el not in "1234567890":
            a += el
    return a
