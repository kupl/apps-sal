from collections import defaultdict


def get_dest(start, w, h):
    if start[0] == 1:
        return (str(start[1]), str(h))
    else:
        return (str(w), str(start[1]))


(n, w, h) = [int(x) for x in input().split()]
dancers = []
groups = defaultdict(list)
destinations = [None for x in range(n)]
for ii in range(n):
    (g, p, t) = [int(x) for x in input().split()]
    dancers.append((g, p, t))
    groups[p - t].append(ii)
for gg in list(groups.values()):
    (V, H) = ([], [])
    for ii in gg:
        dancer = dancers[ii]
        if dancer[0] == 1:
            V.append(dancer)
        else:
            H.append(dancer)
    V.sort(key=lambda x: -x[1])
    H.sort(key=lambda x: x[1])
    table = {orig: get_dest(new, w, h) for (orig, new) in zip(V + H, H + V)}
    for ii in gg:
        destinations[ii] = table[dancers[ii]]
for dd in destinations:
    print(' '.join(dd))
