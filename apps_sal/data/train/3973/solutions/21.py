def remove_char(s):
    l = list(s)
    del (l[0], l[len(l) - 1])
    return "".join(l)
