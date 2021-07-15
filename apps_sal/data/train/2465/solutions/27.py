class Solution:
    @lru_cache(None)
    def divisorGame(self, N: int) -> bool:
        if N == 1:
            return False
        return any(not self.divisorGame(N-x) if N % x == 0 else False for x in range(1, N))
