from itertools import combinations
from math import hypot


def peaceful_yard(yard, min_distance):
    l, yard = len(yard[0]), "".join(yard)
    cats = (divmod(yard.index(c), l) for c in "LMR" if c in yard)
    distances = (hypot(x2-x1, y2-y1) for (x1, y1), (x2, y2) in combinations(cats, 2))
    return all(min_distance <= d for d in distances)
    

# one-liner
#peaceful_yard = lambda y, m: all(m <= d for d in (hypot(x2-x1, y2-y1) for (x1, y1), (x2, y2) in combinations((divmod(i, len(y[0])) for i, c in enumerate("".join(y)) if c != "-"), 2)))

# alternatives:
# more intuitive but much slower:
#    cats = [divmod(i, l) for i, c in enumerate(yard) if c != "-"]
# less readable but avoid imports:
#    distances = [((x2-x1)**2 + (y2-y1)**2)**0.5 for i, (x1, y1) in enumerate(cats, 1) for (x2, y2) in cats[i:]]

