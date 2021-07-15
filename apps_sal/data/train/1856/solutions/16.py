class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        queue, visited, n = collections.deque([( (0, 0), (0, 1), 0)]), set(), len(grid)
        target = ((n-1, n-2), (n-1, n-1))
        while queue:
            (r1, c1), (r2, c2), steps = queue.popleft()
            if ((r1, c1), (r2, c2))==target:
                return steps
            if ((r1, c1), (r2, c2)) in visited:
                continue
            visited |= {((r1, c1), (r2, c2))}
            # vertical
            if c1 + 1 < n and grid[r1][c1+1] == 0 and c2 + 1 < n and grid[r2][c2+1] == 0:
                queue.append(((r1, c1 + 1), (r2, c2 + 1), steps+1))
            # horizontal
            if r1 + 1 < n and grid[r1+1][c1] == 0 and r2 + 1 < n and grid[r2+1][c2] == 0:
                queue.append(((r1 + 1, c1), (r2 + 1, c2), steps+1))
            # vertical
            if r1 == r2 and r1 + 1 < n and grid[r1+1][c1] + grid[r1+1][c1+1] == 0 :
                queue.append(((r1, c1), (r1 + 1, c1), steps+1))
            if c1 == c2 and c1 + 1 < n and grid[r1][c1+1] + grid[r1+1][c1+1] == 0:
                queue.append(((r1, c1), (r1, c1 + 1), steps+1))
        return -1
