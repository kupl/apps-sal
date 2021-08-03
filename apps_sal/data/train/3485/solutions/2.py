s = '''| Honey   | H | 1.36 |
| Water   | W | 1.00 |
| Alcohol | A | 0.87 |
| Oil     | O | 0.80 |'''


def separate_liquids(glass):
    d = {}
    for x in s.split('\n'):
        res = x.split('|')
        a, b = [c.strip(' ') for i, c in enumerate(res) if i in (2, 3)]
        d[a] = float(b)
    l = []
    for x in glass:
        l.extend(x)
    result = iter(sorted(l, key=lambda x: d[x]))

    for x in range(len(glass)):
        for i in range(len(glass[-1])):
            glass[x][i] = next(result)
    return glass
