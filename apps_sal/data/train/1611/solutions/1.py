import re
from collections import defaultdict, deque


def magic_call_depth_number(s):
    adjacent = defaultdict(list)
    for i, j, k in re.findall(r'(p\d+)(.+?)(q)', s):
        for n in re.findall(r'P\d+', j):
            adjacent[i.upper()].append(n)

    s, depths = re.sub(r'p.+?q', '', s), []

    def BFS(start):
        Q = deque([[start, 1, []]])
        while Q:
            node, depth, path = Q.popleft()
            path.append(node)
            if not adjacent[node]:
                depths.append(0)
            for i in adjacent[node]:
                if i not in path:
                    Q.append([i, depth + 1, path[:]])
                else:
                    depths.append(depth)

    [BFS(i) for i in re.findall(r'P\d+', s)]
    return [min(depths), max(depths)] if depths else [0, 0]
