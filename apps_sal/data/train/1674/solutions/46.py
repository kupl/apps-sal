class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        p = [0]
        cur = 0
        for i in piles:
            cur += i
            p.append(cur)
        
        n = len(piles)
        from functools import lru_cache
        @lru_cache(None)
        def dp(start, m):
            if start >= n: return 0
            return max(p[-1] - p[start] - dp(start+i, max(i,m)) for i in range(1,2*m+1))
        return dp(0,1)

