def dont_give_me_five(start,end):
    n = []
    i = start
    while i <= end:
        m = str(i)
        if "5" in m:
            i += 1
        if "5" not in m:
            n.append(m)
            i += 1
    x = len(n)
    return x
