class Solution:

    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        G = [[[], []] for i in range(n)]
        for (i, j) in red_edges:
            G[i][0].append(j)
        for (i, j) in blue_edges:
            G[i][1].append(j)
        res = [[0, 0]] + [[2 * n, 2 * n] for i in range(n - 1)]
        bfs = [[0, 0], [0, 1]]
        while len(bfs) > 0:
            (node, color) = bfs.pop(0)
            for j in G[node][color]:
                if res[j][color] == 2 * n:
                    res[j][color] = res[node][1 - color] + 1
                    bfs.append([j, 1 - color])
        return [x if x != n * 2 else -1 for x in map(min, res)]
