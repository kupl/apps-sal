class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(A), len(A[0])
        
        visited = set()
        outliners_1, outliners_2 = set(), set()
        
        def dfs(curr_i, curr_j, outliners):
            for delta_i, delta_j in moves:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n:
                    if A[next_i][next_j] == 0:
                        outliners.add((curr_i, curr_j))
                    else:
                        if (next_i, next_j) not in visited:
                            visited.add((next_i, next_j))
                            dfs(next_i, next_j, outliners)
        
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    if (i, j) not in visited:
                        if not outliners_1:
                            visited.add((i, j))
                            dfs(i, j, outliners_1)
                        else:
                            visited.add((i, j))
                            dfs(i, j, outliners_2)

        # actually don't need bfs, since we can either pass 1 or 0, so we can just calculate the Manhatton Distance
        min_dist = float(\"inf\")
        for i, j in outliners_1:
            for k, p in outliners_2:
                min_dist = min(abs(i - k) + abs(j - p)  - 1, min_dist)
        
        return min_dist
