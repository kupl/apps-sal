def alphabetic(s):
    return all(a<=b for a,b in zip(s, s[1:]))
