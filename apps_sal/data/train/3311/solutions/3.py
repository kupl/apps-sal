def reverse_invert(lst):
    r = []
    for i in lst:
        if isinstance(i, int):
            if i < 0:
                i = int(str(i)[1:][::-1])
            else:
                i = -int(str(i)[::-1])
            r.append(i)
    return r
