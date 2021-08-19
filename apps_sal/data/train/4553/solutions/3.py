def find_short(s):
    s = s.split()
    l = min(s, key=len)
    return len(l)
