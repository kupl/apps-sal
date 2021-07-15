
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])
        self.O=0
        def check(r,c,Z):
            if -1<r<R and -1<c<C and (r,c) not in Z :
                return True
            return False
        def bt(r,c,res,Z):
            if grid[r][c]==0:
                self.O = max(self.O,res)
                return
            else:
                a = grid[r][c]
                if check(r+1,c,Z+[(r,c)])==True:
                    bt(r+1,c,res+a,Z+[(r,c)])
                if check(r-1,c,Z+[(r,c)])==True:
                    bt(r-1,c,res+a,Z+[(r,c)])
                if check(r,c+1,Z+[(r,c)])==True:
                    bt(r,c+1,res+a,Z+[(r,c)])
                if check(r,c-1,Z+[(r,c)])==True:
                    bt(r,c-1,res+a,Z+[(r,c)])
                return 

        for i in range(R):
            for j in range(C):
                if grid[i][j]!=0:
                    bt(i,j,0,[])
        return self.O

