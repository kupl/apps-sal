def capitalize(s,ind):
    res = ""
    a = 0
    for i in s:
        if a in ind:
            res += i.upper()
        else:
            res += i
        a += 1
    return res
