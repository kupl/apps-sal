class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2 
        
        dp = [0] * (target + 1)
        
        for stone in stones:
            for i in range(target, stone-1, -1): 
                dp[i] = max(dp[i], dp[i-stone] + stone)
                
        return total - 2*dp[-1]
