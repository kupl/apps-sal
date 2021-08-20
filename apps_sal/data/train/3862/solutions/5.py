def mirror(c, d='abcdefghijklmnopqrstuvwxyz'):
    dd = {i: j for (i, j) in zip(d, d[::-1])}
    return ''.join((dd[i] if i in dd else i for i in c.lower()))
