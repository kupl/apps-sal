def string_clean(s):
    y = ""
    for i in s:
        if i.isnumeric():
            continue
        else:
            y += i
    return y
