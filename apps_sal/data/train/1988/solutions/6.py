class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        # 4:43 10/2/20
        out_ds = defaultdict(list)
        for i, j in red_edges:
            out_ds[i] += [('r', j)]
        for i, j in blue_edges:
            out_ds[i] += [('b', j)]

        # intialize queue, result list and visited list
        q = deque([(None, 0, 0)])
        res = [-1] * n
        visited = []
        while q:
            qq = deque([])

            # visit all nodes in q
            for last_color, e, dist in q:
                visited += [(last_color, e)]

                # specify the distance if hasn't been specified
                if res[e] == -1:
                    res[e] = dist

                # traverse all child nodes
                for color, child in out_ds[e]:

                    # skip visited edges and edges with the same color as last edge
                    if color == last_color or (color, child) in visited:
                        continue

                    # add child nodes to a new queue
                    qq += [(color, child, dist + 1)]
            q = qq

        return res
