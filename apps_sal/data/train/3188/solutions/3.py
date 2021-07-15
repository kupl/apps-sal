def basereduct(x, f=0):
    s = str(x)
    if len(s) == 1:
        return x
    elif f == 150:
        return -1
    elif "9" in s:
        f += 1
        return basereduct(int(s, 11), f)
    else:
        return basereduct(int(s, int(max(s)) + 1), 0)
