class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        \"\"\"
        neighbors=[(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        dp=[[0 for i in range(len(mat[0]))] for i in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                queue=[(i,j)]
                visited=set()
                sm=0
                k=-1
                while queue:
                    if k==K:
                        #print(sm)
                        break
                    for each in range(len(queue)):
                        row,col=queue.pop(0)
                        if (row,col) in visited:
                            continue
                        visited.add((row,col))
                        sm+=mat[row][col]
                        for r,c in neighbors:
                            if 0<=row+r<len(mat) and 0<=col+c<len(mat[0]):
                                queue.append((row+r,col+c))
                    k+=1
                dp[i][j]=sm
        return dp
        \"\"\"
        prefix=[[0 for i in range(len(mat[0])+1)] for i in range(len(mat)+1)]
        for i in range(1,len(prefix)):
            for j in range(1,len(prefix[0])):
                prefix[i][j]=(mat[i-1][j-1]+prefix[i-1][j]+prefix[i][j-1])-prefix[i-1][j-1]
        
        
        ans=[[0 for i in range(len(mat[0]))] for i in range(len(mat))]
        for i in range(len(ans)):
            for j in range(len(ans[0])):
                r1=max(0,i-K)
                c1=max(0,j-K)
                r2=min(len(mat)-1,i+K)
                c2=min(len(mat[0])-1,j+K)
                
                ans[i][j]=(prefix[r2+1][c2+1]-prefix[r1][c2+1]-prefix[r2+1][c1])+prefix[r1][c1]
        return ans
