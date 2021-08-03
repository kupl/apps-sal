import re


def simplify(p):
    if p[0] not in '-+':
        p = '+' + p
    p = p.replace('-', ' -')
    p = p.replace('+', ' +')
    p = p[1:].split(' ')
    d = {}
    for m in p:
        f = re.search(r'\d+', m)
        n = int(f.group(0)) if f else 1
        if m[0] == '-':
            n = -n
        v = re.search(r'[a-z]+', m).group(0)
        v = ''.join(sorted(v))
        try:
            d[v] += n
            if not d[v]:
                del d[v]
        except KeyError:
            d[v] = n
    res = ''.join(('+' if d[v] > 0 else '-') + (str(abs(d[v])) if abs(d[v]) > 1 else '') + v for v in sorted(d.keys(), key=lambda x: (len(x), x)))
    if res[0] == '+':
        res = res[1:]
    return res
