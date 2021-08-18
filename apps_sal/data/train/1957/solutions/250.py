class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        '''
        Iterative.
        Shortest path = BFS
        '''
        M, N = len(grid), len(grid[0])
        if not grid or not grid[0] or (grid[0][0] and k == 0):
            return -1
        minpath = 0
        queue = collections.deque([(0, 0, k)])
        seen = {(0, 0): k}

        def outOfBound(r, c):
            return not(0 <= r < M) or not(0 <= c < N)

        def wallButRunsOutOfK(r, c, K):
            return (grid[r][c] and not K)

        def seenWithLargerK(r, c, K, seen):
            return (r, c) in seen and seen[(r, c)] >= K

        while queue:
            for _ in range(len(queue)):
                i, j, K = queue.popleft()
                if i == M - 1 and j == N - 1:
                    return minpath
                if grid[i][j]:
                    K -= 1
                for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if outOfBound(r, c) or wallButRunsOutOfK(r, c, K) or seenWithLargerK(r, c, K, seen):
                        continue
                    seen[r, c] = K
                    queue.append((r, c, K))
            minpath += 1
        return -1

        '''
        Recursive with memo
        '''
        M, N = len(grid), len(grid[0])
        memo = {}

        def path(i, j, k):
            if not(0 <= i < M) or not(0 <= j < N) or (grid[i][j] == 1 and k == 0) or grid[i][j] == -1:
                return float('inf')
            if i == M - 1 and j == N - 1:
                return 0
            if (i, j, k) not in memo:
                if grid[i][j] == 1:
                    k -= 1
                orig, grid[i][j] = grid[i][j], -1
                res = float('inf')
                for r, c in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                    res = min(res, path(r, c, k))
                grid[i][j] = orig
                memo[(i, j, k)] = res + 1
            return memo[(i, j, k)]

        min_path = path(0, 0, k)

        return min_path if min_path != float('inf') else -1
