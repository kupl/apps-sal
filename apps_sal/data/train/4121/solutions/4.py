p1 = ['p', 'k', 'a', 's']
p2 = ['P', 'K', 'A', 'S']
ar = ['a', 'A']
sm = ['s', 'S']
pm = ['p', 'P']
cy = ['k', 'K']


def fight_resolve(d, a):
    if d in p1 and a in p1 or (d in p2 and a in p2):
        return -1
    if a in ar:
        return d if d in cy else a
    elif a in pm:
        return d if d in sm else a
    elif a in sm:
        return d if d in ar else a
    elif a in cy:
        return d if d in pm else a
