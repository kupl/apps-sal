import re


def simplify(poly):
    p = {}
    for m in re.findall(r'([+-]?)(\d*)([a-z]+)', poly):
        var = ''.join(sorted(m[2]))
        p[var] = p.get(var, 0) + (-1 if m[0] == '-' else 1) * (int(m[1]) if m[1] != '' else 1)
    poly = ''.join('+-'[p[k] < 0] + str(abs(p[k])) + k for k in sorted(p, key=lambda x: (len(x), x)) if p[k])
    return re.sub('([+-])1(?=[a-z])', r'\1', poly)[poly[0] == '+':]
