class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        root = x
        while self.parent[root] != root:
            root = self.parent[root]

        while x != root:
            tmp = self.parent[x]
            self.parent[x] = root
            x = tmp
        return root

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False

        if self.size[root_a] <= self.size[root_b]:
            self.parent[root_a] = root_b
            self.size[root_b] += self.size[root_a]
        else:
            self.parent[root_b] = root_a
            self.size[root_a] += self.size[root_b]

        return True


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        m = len(grid)
        n = len(grid[0])
        uf = UnionFind(m * n)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    continue

                rc = r * m + c
                for r_off, c_off in directions:
                    new_r, new_c = r + r_off, c + c_off
                    if not (0 <= new_r < len(grid) and 0 <= new_c < len(grid[0])):
                        continue
                    if grid[new_r][new_c] == 1:
                        new_rc = new_r * m + new_c
                        uf.union(rc, new_rc)

        max_area = max(uf.size)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    continue

                rc = r * m + c
                neighbours = set()
                for r_off, c_off in directions:
                    new_r, new_c = r + r_off, c + c_off
                    if not (0 <= new_r < len(grid) and 0 <= new_c < len(grid[0])):
                        continue
                    if grid[new_r][new_c] == 1:
                        new_rc = new_r * m + new_c
                        neighbours.add(uf.find(new_rc))

                max_area = max(max_area, 1 + sum([uf.size[i] for i in neighbours]))

        return max_area
