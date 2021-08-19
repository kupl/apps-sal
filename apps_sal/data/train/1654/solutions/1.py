def solve_runes(runes):
    for c in sorted(set('0123456789') - set(runes)):
        s = runes.replace('?', c).replace('-', ' - ').replace('+', ' + ').replace('*', ' * ').replace('=', ' == ')
        if not any((e[0] == '0' and e != '0' for e in s.split())) and eval(s):
            return int(c)
    return -1
