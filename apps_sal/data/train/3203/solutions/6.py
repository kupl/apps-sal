import re


def parse_mana_cost(m):
    if not m:
        return {}
    if not re.match(r'^[\dwubrg]+$', m, re.I) or '\n' in m:
        return
    r1, r = re.findall(r'[wubrg]', m, re.I), re.search(r'^[0-9]*', m)
    r, d = r.group() if r else '', {}
    if r != '0' and r:
        d['*'] = int(r)
    for i in m[len(r):]:
        d[i.lower()] = d.get(i.lower(), 0) + 1
    return d
