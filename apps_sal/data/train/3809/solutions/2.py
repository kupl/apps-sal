def charCheck(s, mx, spaces):
    res = ''.join((s.split(), s)[spaces])
    return [len(res)<=mx, res[:mx]]
