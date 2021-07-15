def solved(s):
    if len(s)&1:
        s = s[:len(s)//2]+s[len(s)//2+1:]
    return ''.join(sorted(s))
