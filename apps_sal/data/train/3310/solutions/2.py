def score_pole_vault(vaulters):
    (results, k, R) = (sorted([(v['name'], score(v['results'])) for v in vaulters], key=lambda k: k[1]), 0, {})
    for (key, tie) in [('1st', ' (jump-off)'), ('2nd', ' (tie)'), ('3rd', ' (tie)')]:
        if key == '2nd' and k > 1:
            continue
        (mx, r) = (results[-1][1], [])
        while results and results[-1][1] == mx:
            r += [results.pop()[0]]
        k += len(r)
        R[key] = ', '.join(sorted(r)) + tie if len(r) > 1 else r.pop()
        if k >= 3:
            break
    return R


def score(hh):
    return ([(-1, 0)] + [(i, -len(h)) for (i, h) in [(i, h) for (i, h) in enumerate(hh)] if 'O' in h]).pop() + (-sum((j.count('X') for j in hh)),)
