def chameleon(chameleons, desiredColor):
    r=chameleons[:]
    r.pop(desiredColor)
    if max(r)==min(r):
        return max(r)
    d=max(r)-min(r)
    dc=chameleons[desiredColor]+2*min(r)
    if d%3!=0 or d//3>dc:
        return -1
    return max(r)
