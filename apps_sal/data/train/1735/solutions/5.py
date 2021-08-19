from itertools import product
from collections import defaultdict
from heapq import *


def dijkstra(edges, f, t):
    g = defaultdict(list)
    for (l, r, c) in edges:
        g[l].append((c, r))
    (q, seen, mins) = ([(0, f, ())], set(), {f: 0})
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t:
                return (cost, path)
            for (c, v2) in g.get(v1, ()):
                if v2 in seen:
                    continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))
    return (float('inf'), ())


def shallowest_path(river):
    d = {(y, x): v for (y, line) in enumerate(river) for (x, v) in enumerate(line)}
    width = len(river[0])
    height = len(river)
    depthmin = max([min((d[y, x] for y in range(height))) for x in range(width)])
    depths = sorted(set([v for v in list(d.values()) if v >= depthmin]))
    start = (0, -1)
    end = (0, width)
    for depth in depths:
        edges = [(start, (y, 0), 0) for y in range(height) if d[y, 0] <= depth]
        edges += [((y, width - 1), end, 0) for y in range(height) if d[y, width - 1] <= depth]
        for k in product(list(range(height)), list(range(width))):
            if not k in d or d[k] > depth:
                continue
            (y, x) = k
            for k1 in [(y - 1, x - 1), (y - 1, x), (y - 1, x + 1), (y, x - 1), (y, x + 1), (y + 1, x - 1), (y + 1, x), (y + 1, x + 1)]:
                if not k1 in d or d[k1] > depth:
                    continue
                edges.append((k, k1, 1))
        (dist, res0) = dijkstra(edges, start, end)
        if dist == float('inf'):
            continue
        res = []
        while res0:
            (p, res0) = res0
            res.insert(0, p)
        return res[1:-1]
    return []
