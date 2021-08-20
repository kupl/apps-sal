def tram(s, d, o, c=0, m=0):
    return (lambda c: tram(s - 1, d[1:], o[1:], c, m=max(c, m)))(c + o[0] - d[0]) if s else max(c, m)
