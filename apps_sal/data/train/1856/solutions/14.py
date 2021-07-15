class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = collections.deque([(0, 0, 0, 1, 0)])
        visited = {(0, 0, 0, 1)}
        while queue:
            r0, c0, r1, c1, steps = queue.popleft()
            print(r0, c0, r1, c1, steps)
            if r0 == n - 1 and r1 == n - 1 and c0 == n - 2 and c1 == n - 1:
                return steps
            if r0 == r1:
                if 0 <= c1 + 1 < n and not grid[r1][c1 + 1] and (r1, c1, r1, c1 + 1) not in visited:
                    visited.add((r1, c1, r1, c1 + 1))
                    queue.append((r1, c1, r1, c1 + 1, steps + 1))
                if 0 <= r0 + 1 < n and not grid[r0 + 1][c0] and not grid[r1 + 1][c1]:
                    if (r0 + 1, c0, r1 + 1, c1) not in visited:
                        visited.add((r0 + 1, c0, r1 + 1, c1))
                        queue.append((r0 + 1, c0, r1 + 1, c1, steps + 1))
                    if (r0, c0, r0 + 1, c0) not in visited:
                        visited.add((r0, c0, r0 + 1, c0))
                        queue.append((r0, c0, r0 + 1, c0, steps + 1))
            else:
                if 0 <= c0 + 1 < n and not grid[r0][c0 + 1] and not grid[r1][c1 + 1]:
                    if (r0, c0 + 1, r1, c1 + 1) not in visited:
                        visited.add((r0, c0 + 1, r1, c1 + 1))
                        queue.append((r0, c0 + 1, r1, c1 + 1, steps + 1))
                    if (r0, c0, r0, c0 + 1) not in visited:
                        visited.add((r0, c0, r0, c0 + 1))
                        queue.append((r0, c0, r0, c0 + 1, steps + 1))
                if 0 <= r1 + 1 < n and not grid[r1 + 1][c1]:
                    if (r1, c1, r1 + 1, c1) not in visited:
                        visited.add((r1, c1, r1 + 1, c1))
                        queue.append((r1, c1, r1 + 1, c1, steps + 1))
        
        return -1
