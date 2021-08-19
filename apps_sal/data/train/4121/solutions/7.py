def fight_resolve(d, a):
    return d.islower() ^ a.islower() and (a, d)[(d + a).lower() in 'aspka'] or -1
