def encode(s):
    lst = sorted( s[i or len(s):] + s[:i or len(s)] for i in reversed(range(len(s))) )
    return ''.join(ss[-1] for ss in lst), s and lst.index(s) or 0

def decode(s, n):
    out, lst = [], sorted((c,i) for i,c in enumerate(s))
    for _ in range(len(s)):
        c,n = lst[n]
        out.append(c)
    return ''.join(out)
