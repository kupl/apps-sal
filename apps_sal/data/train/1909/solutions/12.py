class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        #depth search
        N = len(grid)
        M = len(grid[0])
        row = copy.deepcopy(grid)
        col = copy.deepcopy(grid)
        for i in range(N):
            start = M
            prev = 0
            for j in range(M):
                if not prev and grid[i][j]:
                    start = j
                elif prev and not grid[i][j]:
                    row[i][start:j] = list(range(j-start,0,-1))
                    start = M
                prev = grid[i][j]
            row[i][start:M] = list(range(M-start,0,-1))
        for i in range(M):
            start = N
            prev = 0
            for j in range(N):
                if not prev and grid[j][i]:
                    start = j
                elif prev and not grid[j][i]:
                    for k in range(j-start):
                        col[start+k][i] = j-start-k
                    start = N
                prev = grid[j][i]
            for k in range(N-start):
                col[start+k][i] = N-start-k
        maxS = 0
        for i in range(N):
            for j in range(M):
                mS = min(row[i][j], col[i][j])
                for k in range(mS, 0, -1):
                    if k <= maxS:
                        break
                    if row[i+k-1][j] >= k and col[i][j+k-1] >= k:
                        maxS = k
        return maxS*maxS

