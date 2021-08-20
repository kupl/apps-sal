class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        nrows = len(grid)
        ncols = len(grid[0])
        if nrows == 1 and ncols == 1:
            return 0
        step = 1
        if k > nrows - 1 + ncols - 1:
            return nrows - 1 + ncols - 1
        q = collections.deque()
        visited = set([(0, 0, k)])
        q.append((0, 0, k, step))

        def neigh(x, y):
            tocheck = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
            nlist = []
            for n in tocheck:
                if 0 <= n[0] < nrows and 0 <= n[1] < ncols:
                    nlist.append(n)
            return nlist
        while q:
            (i, j, k, step) = q.popleft()
            neighs = neigh(i, j)
            if i == nrows - 1 and j == ncols - 1:
                return step
            if neighs:
                for n in neighs:
                    if grid[n[0]][n[1]] == 1 and k > 0 and ((n[0], n[1], k - 1) not in visited):
                        q.append((n[0], n[1], k - 1, step + 1))
                        visited.add((n[0], n[1], k - 1))
                    if grid[n[0]][n[1]] == 0 and (n[0], n[1], k) not in visited:
                        if n[0] == nrows - 1 and n[1] == ncols - 1:
                            return step
                        q.append((n[0], n[1], k, step + 1))
                        visited.add((n[0], n[1], k))
        return -1
