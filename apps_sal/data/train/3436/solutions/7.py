def err_bob(s):
    (t, a) = ('', 'aeioubcdfghjklmnpqrstvwxyz')
    for (i, c) in enumerate(s + ' '):
        if c.lower() not in a and s[i - 1].lower() in a[5:]:
            t += 'ERR' if s[i - 1].isupper() else 'err'
        t += c
    return t[:-1]
