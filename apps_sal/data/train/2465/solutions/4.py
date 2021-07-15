class Solution:
    def divisorGame(self, N: int) -> bool:
        memo = [None]*(N+1)
        ans = self.canWin(N, memo)
        return ans
        
    def canWin(self, N, memo) :
        if N<=1 :
            return False
        if memo[N] is not None :
            return memo[N]
        for i in range(1, N//2 + 1) :
            if N%i == 0 :
                if not self.canWin(N-i, memo) :
                    memo[N] = True
                    return True
        memo[N] = False
        return False
        
        
        

