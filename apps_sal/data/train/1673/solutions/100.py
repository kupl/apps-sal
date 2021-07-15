class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        m,n=len(arr),len(arr[0])
        for i in range(1,m):
            for j in range(n):
                m=float('inf')
                for k in range(n):
                    if k==j:
                        continue
                    m=min(m,arr[i-1][k])
                arr[i][j]+=m
        return min(arr[-1])
