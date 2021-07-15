class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        if m == 0: return 0
        n = len(mat[0])
        if n == 0: return 0
        
        a = [None for _ in range(m)]
        for i in range(m):
            a[i] = []
            for j in range(n):
                a[i].append([0, 0])
        
        for i in range(m):
            for j in range(n-1, -1, -1):
                if i == n-1:
                    a[i][j][0] = 1 if mat[i][j] == 1 else 0
                else:
                    a[i][j][0] = 1 + a[i-1][j][0] if mat[i][j] == 1 else 0
        
        for j in range(n):
            for i in range(m):
                if i == 0:
                    a[i][j][1] = 1 if mat[i][j] == 1 else 0
                else:
                    a[i][j][1] = 1 + a[i-1][j][1] if mat[i][j] == 1 else 0
        
        ans = 0
        for i in range(m):
            j = 0
            while j < n:
                if mat[i][j] == 0:
                    j += 1
                else:
                    minH = a[i][j][1]
                    k = j
                    while k < n and mat[i][k] == 1:
                        minH = min(minH, a[i][k][1])
                        ans += minH
                        k += 1
                    j += 1
        return ans
                    

