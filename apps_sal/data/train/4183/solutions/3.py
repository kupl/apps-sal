from collections import defaultdict

def greatest_distance(a):
    d = defaultdict(list)
    for i, x in enumerate(a):
        d[x].append(i)
    return max(x[-1] - x[0] for x in d.values())
