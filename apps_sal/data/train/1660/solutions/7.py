import re
def simplify(p):
    p,d = p.strip('+'),{}
    p = re.sub(r'([-+])', r' \1 ', p).split()
    start = 0 if p[0] != '-' else 1
    for i in range(start, len(p), 2):
        find = next(k for k in range(len(p[i])) if p[i][k].isalpha())
        digits = int(p[i][:find] or 1)
        digits = -digits if p[i - 1] == '-' else digits
        to_find = "".join(sorted(p[i][find:]))
        d[to_find] = d.get(to_find, 0) + digits
    li = [[i, j] for i, j in d.items() if j != 0]
    o= sorted(li, key=lambda x: (len(x[0]), x[0]))
    return re.sub(r'(-|\+)\1+', r'\1', "".join([['+', '-'][j < 0] + (str(j) if j not in [1, -1] else '') + i for i, j in o]).strip('+'))
