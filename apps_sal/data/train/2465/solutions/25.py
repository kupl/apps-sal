class Solution:
    def divisorGame(self, N: int) -> bool:
        
        if N <= 3:
            return (N % 2) == 0
        
        dp = [False for _ in range(N+1)]
        dp[2] = True
        
        for i in range(3, N+1):
            for j in range(1, i):
                if i % j == 0 and dp[i-j] == False:
                    dp[i] = True
                    break
                    
        return dp[-1]
                    
        
        

