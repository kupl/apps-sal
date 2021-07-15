def solution(*s):
    s = sorted(s, key=lambda x: len(x))
    return s[0] + s[1] + s[0]
