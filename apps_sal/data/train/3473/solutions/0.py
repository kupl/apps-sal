def doubles(s):
    cs = []
    for c in s:
        if cs and cs[-1] == c:
            cs.pop()
        else:
            cs.append(c)
    return ''.join(cs)
