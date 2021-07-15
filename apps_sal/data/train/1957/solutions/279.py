class Solution:
    # O(m x n) time, O(m x n) space
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        DELTAS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        EMPTY = 0
        m, n = len(grid), len(grid[0])
        q = deque([(0, 0, 0, 0)])
        seen = defaultdict(lambda: float(\"inf\"))
        seen[0, 0] = 0
        
        def is_valid(i, j):
            return 0 <= i < m and 0 <= j < n
        
        while q:
            i, j, step, removal = q.popleft()
            if i == m - 1 and j == n - 1:
                return step
            for di, dj in DELTAS:
                i1, j1 = i + di, j + dj
                if is_valid(i1, j1):
                    if grid[i1][j1] == EMPTY and removal < seen[i1, j1]:
                        seen[i1, j1] = removal
                        q.append((i1, j1, step + 1, removal))
                    elif removal < k and removal + 1 < seen[i1, j1]:  # Not empty but still removable
                        seen[i1, j1] = removal + 1
                        q.append((i1, j1, step + 1, removal + 1))
        
        return -1
                        
            
