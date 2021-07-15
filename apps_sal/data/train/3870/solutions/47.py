def solve(s):
    f = [i for i in range(len(s))if s[i]==' ']
    s = s.replace(' ','')[::-1]
    g = ''
    for i in range(len(s)):
        if i in f:
            g += ' ' + s[i]
            f = list(map(lambda x: x-1, f[1:]))
        else:
            g += s[i]
    return g + (' ' if f else '')
