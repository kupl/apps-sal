class Solution:
    def dfs(self, A,i,j,replace):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
            return
        if A[i][j] == 0 or A[i][j] == replace:
            return
        A[i][j] = replace
        r = self.dfs(A,i+1,j,replace)
        d = self.dfs(A,i,j+1,replace)
        u = self.dfs(A,i-1,j,replace)
        l = self.dfs(A,i,j-1,replace)
        return
    
    def find(self,A,i,j,old):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
            return False
        if A[i][j] == -1:
            return True
        if A[i][j] == 0:
            A[i][j] = old+1
            return False
        if A[i][j] == old+1:
            return False
        A[i][j] = old+1
        return self.find(A,i+1,j,old) or self.find(A,i-1,j,old) or self.find(A,i,j+1,old) or self.find(A,i,j-1,old)

        
    def shortestBridge(self, A: List[List[int]]) -> int:
        iindex = 0
        i,j = 0,0
        replace = -1
        start = ()
        while i < len(A):
            j=0
            while j < len(A[0]):
                if A[i][j] == 1:
                    self.dfs(A,i,j,replace)
                    iindex+=1
                    replace=-2
                    start = (i,j)
                j+=1
            i+=1
        old=1
        while True:
            #print(A)
            if self.find(A,start[0],start[1],old):
                break
            old+=1
        return old-1
