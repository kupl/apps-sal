class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m =len(mat)
        n = len(mat[0])
        arr=[]
        for i in range(m):
            temp=[]
            for j in range(n):
                s=0
                
                r_s=i-k
                r_e=i+k+1
                if r_s<0:
                    r_s=0
                if r_e>m:
                    r_e=m
                c_s=j-k
                c_e=j+k+1
                if c_s<0:
                    c_s=0
                if c_e>n:
                    c_e=n
                for ki in range(r_s,r_e):
                    for l in range(c_s,c_e):
                        s=mat[ki][l]+s
                temp.append(s)
            arr.append(temp)
        return arr
                

