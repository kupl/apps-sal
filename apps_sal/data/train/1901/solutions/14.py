class UnionFind:
    def __init__(self, N):
        self.parents = [i for i in range(N)]
        self.size = [1] * N

    def find(self, x):
        root = x
        while root != self.parents[root]:
            root = self.parents[root]

        while x != root:
            parent = self.parents[x]
            self.parents[x] = root
            x = parent

        return root

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False

        if self.size[root_a] <= self.size[root_b]:
            self.parents[root_a] = root_b
            self.size[root_b] += self.size[root_a]
        else:
            self.parents[root_b] = root_a
            self.size[root_a] += self.size[root_b]

        return True


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # assuming we have a UnionFind data structure

        def rc2idx(r, c):
            return r * n + c

        # build uf out of the islands
        uf = UnionFind(m * n)
        max_area = 0
        for r in range(m):
            for c in range(n):
                # union with the neighbours
                if grid[r][c] == 1:
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = r + dr, c + dc
                        if not (0 <= nr < m and 0 <= nc < n):
                            continue
                        if grid[nr][nc] == 1:
                            uf.union(rc2idx(r, c), rc2idx(nr, nc))

                    max_area = max(max_area, uf.size[uf.find(rc2idx(r, c))])

        # check all possible points for setting 0 to 1
        for r in range(m):
            for c in range(n):
                area = 0
                if grid[r][c] == 0:
                    area = 1
                    unique_neis = set()
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = r + dr, c + dc
                        if not (0 <= nr < m and 0 <= nc < n):
                            continue
                        if grid[nr][nc] == 1:
                            island = uf.find(rc2idx(nr, nc))
                            unique_neis.add(island)

                    area += sum([uf.size[island] for island in unique_neis])

                max_area = max(max_area, area)

        return max_area
