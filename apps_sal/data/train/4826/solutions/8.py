from re import compile
count = compile('[a-zA-Z][|};&#[\\]\\/><()*]{2}0[|};&#[\\]\\/><()*]{2}0[|};&#[\\]\\/><()*]{2}[a-zA-Z]').findall
auto = compile('(?i)automatik').search
mecha = compile('(?i)mechanik').search


def count_robots(a):
    x = y = 0
    for s in a:
        if auto(s):
            x += len(count(s))
        elif mecha(s):
            y += len(count(s))
    return [f'{x} robots functioning automatik', f'{y} robots dancing mechanik']
