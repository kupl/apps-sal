def solve(f):
    return (lambda l: (lambda d: sorted([e for e in d if d[e] == max(d.values())]))({e: l.count(e) for e in set(l)}))([e[e.rfind('.'):] for e in f])
