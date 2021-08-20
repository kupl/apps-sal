class Solution:

    @lru_cache(None)
    def divisorGame(self, N: int) -> bool:
        if N == 0:
            return False
        if N == 1:
            return False
        if N == 2:
            return True

        @lru_cache(None)
        def divs(N):
            out = []
            for i in range(1, N // 2 + 1):
                if N % i == 0:
                    out.append(i)
            return out
        moves = divs(N)
        for move in moves:
            if not self.divisorGame(N - move):
                return True
        return False
