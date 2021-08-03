class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        '''
            node, depth, k
        '''

        R, C = len(grid), len(grid[0])

        def neighbors(r, c):
            for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        target = (R - 1, C - 1)
        q = deque([((0, 0), 0, k)])

        seen = set()

        while q:
            node, depth, k = q.popleft()
            if (node, k) not in seen:
                seen.add((node, k))

                if node == target:
                    return depth

                for r, c in neighbors(*node):
                    if grid[r][c] == 1 and k > 0:
                        q.append(((r, c), depth + 1, k - 1))
                    elif grid[r][c] == 0:
                        q.append(((r, c), depth + 1, k))

        return -1
