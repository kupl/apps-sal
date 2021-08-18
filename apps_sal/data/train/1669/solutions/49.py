class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        dp = defaultdict(list)

        for e in sorted(hand):
            dp[e].append(dp[e - 1].pop() + 1) if len(dp[e - 1]) != 0 else dp[e].append(1)
            if dp[e] and dp[e][-1] == W:
                dp[e].pop()

        return all(len(e) == 0 for e in list(dp.values()))
