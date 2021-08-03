# So the basic idea here is that there is no reason to have separate sum_alex and sum_lee variables, because they both sum up to suffix_sum[pile]
# Here is an example (X - we haven't desided yet, A - taken by Alex, L - taken by Lee)

# XXXXXXXXXXAALAAALLLAALA
#           ^
# \t\t  pile
# From this you can see that in order to calculate the number of piles taken by this player so far we just substract the number of the piles taken by another player from the total number of piles up to the current pile position.
# The next important thing to notice is that minimizing sum for the one player leads to maximising it for another and vice versa.
# This leads us to conclusion that we can do the same with just a single variable sum_next_player.
# The alrorightm now looks the following way:

# We're trying to pick up to 2 * M piles from the current position and pass the turn to the next player
# We're getting back from the next player the maximum sum they were able to get and trying to minimize it
# Now when we found the minimum sum for the other player that also means we found the maximum sum for us, so return it
# That's how we got to the nice and short Top-Down DP solution.
# The only thing left - convert it to Bottom-Up solution to make the interviewer happy. And here is it

class Solution:
    @staticmethod
    def _suffix_sum(piles: List[int]) -> List[int]:
        suffix_sum = [0]

        for pile in reversed(piles):
            suffix_sum.append(suffix_sum[-1] + pile)

        suffix_sum.reverse()

        return suffix_sum

    def stoneGameII(self, piles: List[int]) -> int:
        suffix_sum = self._suffix_sum(piles)

        dp = [[0] * (len(piles) + 1) for _ in range(len(piles) + 1)]

        for pile in reversed(range(len(piles))):
            for M in reversed(range(len(piles))):
                sum_next_player = suffix_sum[pile]

                for next_pile in range(pile + 1, min(pile + 2 * M + 1, len(piles) + 1)):
                    sum_next_player = min(
                        sum_next_player, dp[next_pile][max(M, next_pile - pile)]
                    )

                sum_player = suffix_sum[pile] - sum_next_player

                dp[pile][M] = sum_player

        return dp[0][1]
