class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        
        
        
        # my solution ... 464 ms ... 70 % ... 15.5 MB ... 0 %
        #  time: O(n*m*min(n,m))
        # space: O(n*m)
        
        def func(i, j):
            res = 0
            height = float('inf')
            for jj in range(j, -1, -1):
                height = min(height, cnt[i][jj][1])
                if not height:
                    break
                res += height  # 【(i,jj)为左下角，(i,j)为右下角】的矩形个数
            return res
        
        n, m = len(mat), len(mat[0])
        cnt = [[0]*m for _ in range(n)]
        tot = 0
        for i in range(n):
            for j in range(m):
                if not mat[i][j]:
                    cnt[i][j] = (0, 0)  # cnt[i][j] = (ij及左侧1的个数，ij及上方1的个数)
                else:
                    lft = cnt[i][j-1][0] + 1 if j > 0 else 1
                    top = cnt[i-1][j][1] + 1 if i > 0 else 1
                    cnt[i][j] = (lft, top)
                    tot += func(i, j)
        return tot
        
        

