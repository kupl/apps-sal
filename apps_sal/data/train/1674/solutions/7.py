class Solution:

    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        cache = {}

        def recursive_game(start, M):
            score_left = sum(piles[start:])
            if start >= N:
                return 0
            if (start, M) in cache:
                return cache[start, M]
            if start + 2 * M >= N:
                return score_left
            my_score = 0
            for x in range(1, 2 * M + 1):
                opponent_score = recursive_game(start + x, max(M, x))
                my_score = max(my_score, score_left - opponent_score)
            cache[start, M] = my_score
            return my_score
        return recursive_game(0, 1)
