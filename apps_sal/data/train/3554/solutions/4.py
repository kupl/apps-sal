from itertools import groupby


def get_score(a):
    s = 0
    if set(a) == set([1, 2, 3, 4, 5, 6]):
        s = 1000
    elif len(set([i * 10 if i == 1 else i for i in a if a.count(i) == 2])) == 3:
        s = 750
    else:
        s += sum((sum(set([i * 10 if i == 1 else i for i in a if a.count(i) == k])) * 100 * (k - 2) for k in (3, 4, 5, 6)))
        s += sum(((i * 10 if i == 1 else i) * a.count(i) for i in (1, 5) if a.count(i) in (1, 2))) * 10
    return s if s != 0 else 'Zonk'
