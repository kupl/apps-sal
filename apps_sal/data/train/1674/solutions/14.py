import functools
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        for i in range(n-2, -1, -1):
            piles[i] += piles[i+1] # suffix sum
        
        # 在位置i，M=m的情况下，当前选手获得的最大分数
        @lru_cache(None)
        def dp(i, m):
            if i+2*m >= n: return piles[i]
            #                      在当前player选择x下，对手能得到的最大分数
            # 选择了x，就是给对方设置了M
            # return piles[i] - min([dp(i+x, max(m,x)) for x in range(1, 2*m+1)])
            # 写成这样更清晰
            res = 0
            for x in range(1, 2*m+1):
                res = max(res, piles[i] - dp(i+x, max(m,x)))
            return res
        return dp(0, 1)
