def solve(c):
    k = ''.join(reversed(c))
    h = k.replace(' ', '')
    s = [i for i in range(len(c)) if ' ' == c[i]]
    h = list(h)
    for i in range(len(c)):
        if i in s:
            h.insert(i, ' ')
    return ''.join(h)
