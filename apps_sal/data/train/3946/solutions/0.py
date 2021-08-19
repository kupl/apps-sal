def interweave(s1, s2):
    s = [''] * (len(s1) + len(s2))
    (s[::2], s[1::2]) = (s1, s2)
    return ''.join((c for c in s if not c.isdigit())).strip()
