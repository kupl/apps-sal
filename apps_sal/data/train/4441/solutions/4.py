def chmod_calculator(p):
    d = {'r': 4, 'w': 2, 'x': 1, '-': 0}
    ob = {'user': '0', 'group': '0', 'other': '0'}
    for i, j in p.items():
        ob[i] = str(sum(map(lambda x: d[x], j)))
    return ''.join(ob.values())
