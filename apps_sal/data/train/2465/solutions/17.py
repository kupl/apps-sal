class Solution:
    @lru_cache(maxsize=None)
    def divisorGame(self, N: int) -> bool:
        if N == 2:
            return True

        options = []

        for x in range(1, N // 2):
            if N % x == 0:
                options.append(N - x)

        return any(map(
            lambda x: not self.divisorGame(x),
            options,
        ))
