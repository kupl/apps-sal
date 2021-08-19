import re


def solve_runes(runes):
    for i in sorted(set(''.join([str(i) for i in range(10)])) - set(runes)):
        var = runes.replace('?', i)
        if re.search('([^\\d]|\\b)0\\d+', var):
            continue
        (expr, result) = var.split('=')
        if eval(expr) == eval(result):
            return int(i)
    return -1
