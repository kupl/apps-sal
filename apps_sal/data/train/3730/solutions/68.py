def capitalize(s):
    s1 = ''.join(a.upper() if i % 2 == 0 else a for i,a in enumerate(s))
    s2 = ''.join(a.upper() if i % 2 != 0 else a for i,a in enumerate(s))
    return [s1,s2]
