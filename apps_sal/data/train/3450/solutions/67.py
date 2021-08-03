def array(p):
    print(p)
    astring = ""
    s = (p.replace(" ", "")).split(",")
    print(s)
    if len(s) < 3:
        return None
    for i in range(0, len(s) - 1):
        if i == 0:
            pass
        else:
            astring += s[i] + " "
    ansr = astring.rstrip()
    return ansr
