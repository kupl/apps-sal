class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        
        m=len(arr)
        
        for i in range(1,m):
            for j in range(m):
                res=float('inf')
                for x in range(m):
                    val=arr[i][j]+arr[i-1][x]
                    if x!=j and val<res:
                        res=val
                arr[i][j]=res
                    
        return min(arr[-1])
