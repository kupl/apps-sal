class Solution:
    def shortestAlternatingPaths(self, n: int,
                                 red_edges: List[List[int]],
                                 blue_edges: List[List[int]]) -> List[int]:
        g = {}
        for s, e in red_edges:
            if s not in g:
                g[s] = []
            g[s].append((e, 'r'))
        for s, e in blue_edges:
            if s not in g:
                g[s] = []
            g[s].append((e, 'b'))
        return [find_path_length(g, 0, i) for i in range(0, n)]


def find_path_length(g, s, e):
    to_visit = [(s, 0, 'r'), (s, 0, 'b')]
    visited = set()
    while to_visit:
        x, i, c = to_visit.pop(0)
        if (x, c) in visited:
            continue
        visited.add((x, c))
        if x == e:
            return i
        if x not in g:
            continue
        for s1, c1 in g[x]:
            if c != c1:
                to_visit.append((s1, i + 1, c1))
    return -1
