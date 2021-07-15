import re


def solve_runes(runes):
    runes = runes.replace('=', '==')
    s = bool(re.search(r'\b0\d', runes.replace('?', '0')))
    for d in map(str, range(s, 10)):
        if d not in runes and eval(runes.replace('?', d)):
            return int(d)
    return -1
