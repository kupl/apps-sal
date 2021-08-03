class UF:
    def __init__(self, grid):
        N = len(grid[0]) * len(grid)
        self.parent = list(range(N))
        self.size = [0] * N
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    self.size[i * len(grid) + j] = 1

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
            self.parent[a] = self.parent[self.parent[a]]
        return self.parent[a]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            self.parent[pa] = pb
            self.size[pb] += self.size[pa]


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        uf = UF(grid)
        N, M = len(grid), len(grid[0])
        for i in range(N):
            for j in range(M):
                if not grid[i][j]:
                    continue
                for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < N and 0 <= ny < M and grid[nx][ny]:
                        uf.union(i * N + j, nx * N + ny)
        mx = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j]:
                    continue
                all_adjacent = 0
                seen = set()
                for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < N and 0 <= ny < M and grid[nx][ny]:
                        parent = uf.find(nx * N + ny)
                        if parent not in seen:
                            seen.add(parent)
                            all_adjacent += uf.size[parent]
                mx = max(mx, 1 + all_adjacent)
        return max(mx, max(uf.size))
