class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        # adjacent graph, branching for red/blue
        # 0 for red, 1 for blue
        G = [[[], []] for i in range(n)]
        for i, j in red_edges:
            G[i][0].append(j)
        for i, j in blue_edges:
            G[i][1].append(j)
        # Init res, we maintain both path-length for red & blue.
        res = [[0, 0]] + [[2 * n, 2 * n] for i in range(n - 1)]
        # bfs : [[node, red], [node, blue]]
        bfs = [[0, 0], [0, 1]]
        # actual BFS
        while len(bfs) > 0:
            node, color = bfs.pop(0)
            for j in G[node][color]:
                if res[j][color] == 2 * n:
                    res[j][color] = res[node][1 - color] + 1
                    bfs.append([j, 1 - color])

        result = []
        for length in res:
            smaller = min(length)
            if smaller < 2 * n:
                result.append(smaller)
            else:
                result.append(-1)

        return result
