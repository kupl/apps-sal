from itertools import groupby


def ranking(people):
    x = len(str(len(people)))
    rank = 1
    people = sorted(people, key=lambda p: p['points'], reverse=True)
    groups = [[*g[1]] for g in groupby(people, key=lambda p: p['points'])]
    for g in groups:
        for p in g:
            p['position'] = rank
        rank += len(g)
    return sorted(people, key=lambda p: str(p['position']).zfill(x) + p['name'])
