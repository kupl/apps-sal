def double_char(s):
    y = list(s)
    length = len(y)
    ffs = list(range(0, length))
    blank = ""
    for i in ffs:
        blank = blank + y[i] + y[i]
    return blank
