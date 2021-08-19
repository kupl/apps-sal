from collections import defaultdict


def alphabet_war(fight):
    d = defaultdict(int)
    (d['w'], d['p'], d['b'], d['s'], d['m'], d['q'], d['d'], d['z']) = (4, 3, 2, 1, -4, -3, -2, -1)
    a = sum((d[x] for x in fight))
    return 'Left side wins!' if a > 0 else "Let's fight again!" if a == 0 else 'Right side wins!'
