class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}
        n = len(piles)
        
        def dfs(player, start, m):
            if (player, start, m) in memo:
                return memo[(player, start, m)]
            
            cur = 0
            res = 0
            aj = i = start
            am = m
            
            while i < n and i - start + 1 <= 2 * m:
                cur += piles[i]
                _, bj, bm = dfs(1 - player, i + 1, max(i - start + 1, m))
                if res < cur + dfs(player, bj + 1, bm)[0]:
                    res = cur + memo[(player, bj + 1, bm)][0]
                    aj = i
                    am = max(i - start + 1, m)
                    
                i += 1
            
            memo[(player, start, m)] = (res, aj, am)
            return res, aj, am
        
        return dfs(0, 0, 1)[0]

