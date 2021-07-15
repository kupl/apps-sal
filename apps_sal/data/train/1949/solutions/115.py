class Solution:
    def getMaximumGold(self, A: List[List[int]]) -> int:
        def dfs(i,j):
            if not (0<=i<m and 0<=j<n):
                return 0
            if A[i][j]==0:
                return 0
            if (i,j) in path:
                return 0
            path.add((i,j))
            gold=0
            for ni,nj in (i-1,j),(i,j+1),(i+1,j),(i,j-1):
                gold=max(gold,dfs(ni,nj))
            path.discard((i,j))
            return A[i][j]+gold
        
        ans=0
        maxpath=set()
        path=set()
        m,n=len(A),len(A[0])
        for i in range(m):
            for j in range(n):
                if (i,j) in maxpath:
                    pass
                gold=dfs(i,j)
                if gold>ans:
                    ans=gold
                    #maxpath=set(path)
                path.clear()
        
        return ans
