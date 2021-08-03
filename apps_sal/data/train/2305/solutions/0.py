import sys
from collections import deque


def diameter(n, links):
    q = deque([(0, -1)])
    v = 0
    while q:
        v, p = q.popleft()
        q.extend((u, v) for u in links[v] if u != p)

    q = deque([(v, -1)])
    w = 0
    parents = [-1] * n
    while q:
        w, p = q.popleft()
        parents[w] = p
        q.extend((u, w) for u in links[w] if u != p)
    parents_rev = [-1] * n
    p = w
    while parents[p] != -1:
        parents_rev[parents[p]] = p
        p = parents[p]
    return v, w, parents, parents_rev


def construct(s, links, parents, parents_rev):
    v = s
    result = []
    while v != -1:
        pv, rv = parents[v], parents_rev[v]
        child_count = 0
        for u in links[v]:
            if u == pv or u == rv:
                continue
            if len(links[u]) != 1:
                return False
            child_count += 1
        my_value = len(result) + 1
        result.extend(list(range(my_value + 1, my_value + child_count + 1)))
        result.append(my_value)
        v = parents[v]
    return result


def solve(n, links):
    d1, d2, parents, parents_rev = diameter(n, links)
    result1 = construct(d1, links, parents_rev, parents)
    if result1 is False:
        return [-1]
    result2 = construct(d2, links, parents, parents_rev)
    return min(result1, result2)


n = int(input())
links = [set() for _ in range(n)]
INF = 10 ** 9

for line in sys.stdin:
    v, w = list(map(int, line.split()))
    v -= 1
    w -= 1
    links[v].add(w)
    links[w].add(v)

print((*solve(n, links)))
