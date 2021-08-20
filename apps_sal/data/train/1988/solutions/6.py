class Solution:

    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        out_ds = defaultdict(list)
        for (i, j) in red_edges:
            out_ds[i] += [('r', j)]
        for (i, j) in blue_edges:
            out_ds[i] += [('b', j)]
        q = deque([(None, 0, 0)])
        res = [-1] * n
        visited = []
        while q:
            qq = deque([])
            for (last_color, e, dist) in q:
                visited += [(last_color, e)]
                if res[e] == -1:
                    res[e] = dist
                for (color, child) in out_ds[e]:
                    if color == last_color or (color, child) in visited:
                        continue
                    qq += [(color, child, dist + 1)]
            q = qq
        return res
