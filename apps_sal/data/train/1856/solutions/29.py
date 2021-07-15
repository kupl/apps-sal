class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        '''
        BFS
        Time: O(n^2)
        Space: O(n)
        '''
        n = len(grid)
        start = (0, 0, 0)
        end = (n-1, n-2, 0)
        queue = {start}
        seen = set()
        steps = 0
        while queue:
            newQueue = set()
            for i, j, d in queue:
                if (i, j, d) == end: return steps
                seen.add((i, j, d))
                if d == 0:
                    if j + 2 < n and not grid[i][j+2]:
                        if (i, j+1, 0) not in seen: newQueue.add((i, j+1, 0))
                    if i + 1 < n and not grid[i+1][j] and not grid[i+1][j+1]:
                        if (i+1, j, 0) not in seen: newQueue.add((i+1, j, 0))
                        if (i, j, 1) not in seen: newQueue.add((i, j, 1))
                else:
                    if i + 2 < n and not grid[i+2][j]:
                        if (i+1, j, 1) not in seen: newQueue.add((i+1, j, 1))
                    if j + 1 < n and not grid[i][j+1] and not grid[i+1][j+1]:
                        if (i, j+1, 1) not in seen: newQueue.add((i, j+1, 1))
                        if (i, j, 0) not in seen: newQueue.add((i, j, 0))

            queue = newQueue
            steps += 1
        return -1
