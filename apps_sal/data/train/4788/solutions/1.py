G = {str(k): k for k in range(1, 18)}
G['B'] = -2
G['0'] = -1
G['0+'] = 0


def sort_grades(gs):
    return sorted(gs, key=lambda g: G[g[1:]])


G = ['B', '0', '0+'] + [str(g) for g in range(1, 18)]


def sort_grades(gs):
    return sorted(gs, key=lambda g: G.index(g[1:]))
