class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        suffix_sum = [0] * N

        running_sum = 0
        for idx in range(N - 1, -1, -1):
            running_sum += piles[idx]
            suffix_sum[idx] = running_sum

        DP = [[0] * (N) for _ in range(N)]

        for pile_no in reversed(list(range(N))):
            for M in reversed(list(range(N))):
                min_next_player = suffix_sum[pile_no]
                for x in range(1, min(2 * M + 1, N + 1)):
                    if pile_no + x < N:
                        min_next_player = min(min_next_player, DP[pile_no + x][max(x, M)])
                    else:
                        min_next_player = 0
                DP[pile_no][M] = suffix_sum[pile_no] - min_next_player

        return DP[0][1]
