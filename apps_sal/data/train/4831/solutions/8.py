
def solved(s):
    l = len(s)
    s = s[0:l // 2] + s[l // 2 + 1:] if l % 2 else s
    s = list(s)
    s.sort()
    return ''.join(s)
