import re


def split_exp(n):
    r = [n[0:i + 1] + re.sub('\\.0+$', '', re.sub('\\d', '0', n[i + 1:])) for i in range(len(n))]
    r = [re.sub('\\d(?!$)', '0', re.sub('.+(?=\\.)|0+$', '', x)) if '.' in x else re.findall('\\d0*$', x)[0] for x in r]
    rs = []
    for x in r:
        if not (re.match('^[0.]+$', x) or x in rs):
            rs.append(x)
    return rs
