class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:      
        '''
        Observation: 
        Minimum weight stone is equal to the problem of partionining stones into
        two arrays A and B such that | sum(A) - sum(B) | is minimized.
        
        Idea: Given such a partition, we smash the stones as follows. Choose a in A
        and b in B arbitrarily.
          - if a == b: they both are destroyed
          - if a < b: place b - a into B
          - if a > b: place a - b into A
        Can argue that at the end, the stone remaining will have weight which is
        the difference.
        
        Use a knapsack like DP to solve the problem.
        '''
        
        n = len(stones)
        total = sum(stones)
        # memo keeps track of whether or not we can get a sum of exactly T for
        # the smaller of the two sets (thus, T <= sum(A)/2) using numbers
        # from 0 .. i
        memo = {}
        def dp(i, t):
          if (i,t) in memo:
            return memo[i, t]
          
          if i == -1:
            memo[i, t] = t == 0
          elif t < 0:
            memo[i, t] = False
          else:
            memo[i, t] = dp(i-1, t) or dp(i-1, t - stones[i])
          return memo[i, t]
          
        return min(abs(total - 2*t) for t in range(total//2 + 1) if dp(n-1, t))
        
        

