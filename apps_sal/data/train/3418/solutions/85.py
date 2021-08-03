def reverse_list(l):
    r = []
    le = len(l)
    while le > 0:
        r.append(l[le - 1])
        le -= 1
    return r
