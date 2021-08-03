def narcissistic(value):
    vstr = str(value)
    nvalue = sum(int(i)**len(vstr) for i in vstr)
    return nvalue == value
