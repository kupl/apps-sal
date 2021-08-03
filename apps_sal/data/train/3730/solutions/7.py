def capitalize(s):
    s1 = ''.join(s[i].upper() if i % 2 == 0 else s[i] for i in range(0, len(s)))
    s2 = ''.join(s[i].upper() if i % 2 != 0 else s[i] for i in range(0, len(s)))
    return [s1, s2]
