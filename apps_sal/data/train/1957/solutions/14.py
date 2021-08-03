import collections


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        self.g = grid

        q = collections.deque()
        dist = {
            (0, 0): [0] * (k + 1)
        }

        minDist = {
            (0, 0): 0
        }

        q.append((0, 0, 0))
        target = (len(grid) - 1, len(grid[0]) - 1)

        while q:
            node = q.popleft()

            nodeDist = dist[(node[0], node[1])][node[2]]

            for n in self.neigh(node):
                nk = node[2] + (1 if grid[n[0]][n[1]] == 1 else 0)

                if n not in dist:
                    dist[n] = [None] * (k + 1)

                if nk <= k and dist[n][nk] is None:
                    neighDist = nodeDist + 1

                    found = False
                    for i in range(0, nk):
                        if dist[n][i] is not None and dist[n][i] <= neighDist:
                            found = True

                    if not found:
                        dist[n][nk] = nodeDist + 1
                        minDist[n] = min(minDist[n], dist[n][nk]) if n in minDist else dist[n][nk]
                        q.append((n[0], n[1], nk))

        # print(dist)

        return minDist[target] if target in minDist else -1

    def neigh(self, pos):
        cand = [
            (pos[0] + 1, pos[1]),
            (pos[0] - 1, pos[1]),
            (pos[0], pos[1] + 1),
            (pos[0], pos[1] - 1)
        ]

        out = []

        for c in cand:
            if c[0] >= 0 and c[0] < len(self.g) and c[1] >= 0 and c[1] < len(self.g[0]):
                out.append(c)

        return out
