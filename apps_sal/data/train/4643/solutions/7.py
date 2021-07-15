def zipvalidate(p):
    return len(p)==6 and p[0] in '12346' and all(d in '0123456789' for d in p)
