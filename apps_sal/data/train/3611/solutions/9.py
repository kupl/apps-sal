def ranking(people):
    pnt = None
    res = []
    for (c, d) in enumerate(sorted(people, key=lambda d: (-d['points'], d['name'])), 1):
        if pnt != d['points']:
            pnt = d['points']
            pos = c
        res.append(dict({'position': pos}, **d))
    return res
