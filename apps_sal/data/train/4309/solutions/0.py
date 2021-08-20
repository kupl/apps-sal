from itertools import groupby


def replace(s):
    (queue, rle) = ({}, [[i, k, len(list(g))] for (i, (k, g)) in enumerate(groupby(s))])
    for (i, k, l) in reversed(rle):
        if l not in queue:
            queue[l] = {}
        queue[l].setdefault(k, []).append(i)
    for l in queue:
        while sum(map(bool, queue[l].values())) > 1:
            for c in queue[l]:
                rle[queue[l][c].pop()][1] = ' '
    return ''.join((k * l for (i, k, l) in rle))
