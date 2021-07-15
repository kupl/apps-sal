def encode(s):
    if not s:return('',0)
    l=sorted(s[-i:]+s[:-i]for i in range(len(s)))
    return(''.join(x[-1]for x in l),l.index(s))

def decode(s, n):
    if not s:return s
    l=['']*len(s)
    for _ in range(len(s)):
        l=sorted(s[i]+l[i]for i in range(len(s)))
    return l[n]
