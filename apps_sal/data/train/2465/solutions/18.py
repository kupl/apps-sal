class Solution:
    def __init__(self):
        self.memo = {}
    def findfactors(self, N):
        n = N//2
        fs = []
        for i in range(2, n+1):
            if N%i==0:
                fs.append(i)
        return fs+[1]
    
    def div(self, N):
        if N in self.memo:
            return self.memo[N]
        fs = self.findfactors(N)
        if N==1:
            self.memo[N] = 0
            return 0
        else:
            nf = len(fs)
            vals = [0]*nf
            for i in range(nf):
                vals[i] = self.div(N-fs[i])
            self.memo[N] = 1+max(vals)
            return self.memo[N]
    
    def divisorGame(self, N: int) -> bool:
        ans = self.div(N)
        if ans%2==0:
            return False
        else:
            return True
        

