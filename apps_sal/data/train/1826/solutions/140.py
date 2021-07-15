class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        res=[]
        t=[]
        for i in range(len(mat)):
            t.append([0]*len(mat[0]))
            res.append([0]*len(mat[0]))
            for j in range(len(mat[0])):
                t[i][j]=mat[i][j]
                if j>0:
                    mat[i][j]+=mat[i][j-1]
                    
                
        #print(mat,t)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                s = 0
                top = i-K
                bot = i+K
                left = j-K
                if left<0: left =0
                right = j+K
                if right>=len(mat[0]):
                    right=len(mat[0])-1
                for k in range(top,bot+1):
                    if k>=0 and k<len(mat):
                        s+=(mat[k][right]-mat[k][left]+t[k][left])
                res[i][j]=s
        return res
                
                

