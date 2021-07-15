class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @functools.lru_cache(maxsize=None)
        def minimax(st, m, player):
            if st >= len(piles): return 0
            if player:
                return max([sum(piles[st:st+x]) + minimax(st+x, max(m,x), player^1) for x in range(1, 2*m+1)])
            else:
                return min([minimax(st+x, max(m,x), player^1) for x in range(1, 2*m+1)])
        return minimax(0, 1, 1) 
