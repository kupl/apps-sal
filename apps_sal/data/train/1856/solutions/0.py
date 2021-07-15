class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        queue = deque([(0, 0, True)])
        dists = {(0, 0, True): 0}

        while queue:
            i, j, hor = queue.popleft()
            if (i, j) == (m-1, n-2):
                return dists[(i, j, hor)]
            if hor:
                if j+2 < n and not grid[i][j+2]:
                    if (i, j+1, hor) not in dists:
                        queue.append((i, j+1, hor))
                        dists[(i, j+1, hor)] = dists[(i, j, hor)]+1
                if i+1 < m and not grid[i+1][j] and not grid[i+1][j+1]:
                    if (i+1, j, hor) not in dists:
                        queue.append((i+1, j, hor))
                        dists[(i+1, j, hor)] = dists[(i, j, hor)]+1
                    if (i, j, not hor) not in dists:
                        queue.append((i, j, not hor))
                        dists[(i, j, not hor)] = dists[(i, j, hor)]+1
            else:
                if i+2 < m and not grid[i+2][j]:
                    if (i+1, j, hor) not in dists:
                        queue.append((i+1, j, hor))
                        dists[(i+1, j, hor)] = dists[(i, j, hor)]+1
                if j+1 < n and not grid[i][j+1] and not grid[i+1][j+1]:
                    if (i, j+1, hor) not in dists:
                        queue.append((i, j+1, hor))
                        dists[(i, j+1, hor)] = dists[(i, j, hor)]+1
                    if (i, j, not hor) not in dists:
                        queue.append((i, j, not hor))
                        dists[(i, j, not hor)] = dists[(i, j, hor)]+1
        
        return -1
