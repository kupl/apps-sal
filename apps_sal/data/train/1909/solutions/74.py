class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        # O(m*n*min(m,n))
        up = [[0 for _ in range(len(grid[0])+1)] for _ in range(len(grid)+1)]
        left = [[0 for _ in range(len(grid[0])+1)] for _ in range(len(grid)+1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                    if grid[i][j]:
                        up[i+1][j+1] = up[i][j+1] + 1
                        left[i+1][j+1] = left[i+1][j] + 1
        res = 0       
        for d in up:
            print(d)
        for l in left:
            print(l)
        MAXSQ = min(len(grid[0]), len(grid))
        for i in range(len(grid)):
            for j in range(len(grid[0])):   
                for slen in range(1, MAXSQ+1):
                    if up[i+1][j+1] >= slen and left[i+1][j+1] >= slen and i+1-(slen-1) > 0 and j+1-(slen-1) > 0 and \\
                            up[i+1][j+1-(slen-1)] >= slen and left[i+1-(slen-1)][j+1] >= slen:

                        res = max(res, slen*slen)
                # while i+1-slen > 0 and j+1-slen > 0 and left[i+1-slen][j+1] >= slen and up[i+1][j+1-slen] >= slen:
                #     slen += 1
                    
        return res
                
