import re

def solve_runes(runes):
    for d in '0123456789':
        if d not in runes:
            if d == '0' and (re.search('(^|[+\-*=])\?[?\d]', runes)):
                continue
            expr = runes.replace('?', d).replace('=', '==')
            if eval(expr):
                return int(d)
    return -1
