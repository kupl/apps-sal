def shifted_diff(f, s):
    try:
        ix = s.index(f[0])
        return ix if f==s[ix:]+s[:ix] else -1
    except:
        return -1
