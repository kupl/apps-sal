from collections import defaultdict

def group_in_10s(*xs):
    d = defaultdict(list)
    for x in xs:
        d[x // 10].append(x)
    return [sorted(d[i]) if i in d else None for i in range(max(d) + 1)] if d else []
