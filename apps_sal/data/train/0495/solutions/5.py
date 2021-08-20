import queue


class Solution:

    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        return self.topDown(stones, 0, 0, 0, [[None for s in range(total + 1)] for i in range(len(stones))])

    def topDown(self, stones, idx, sum1, sum2, memo):
        if idx >= len(stones):
            return abs(sum1 - sum2)
        if memo[idx][sum1] != None:
            return memo[idx][sum1]
        difference_1 = self.topDown(stones, idx + 1, sum1 + stones[idx], sum2, memo)
        difference_2 = self.topDown(stones, idx + 1, sum1, sum2 + stones[idx], memo)
        memo[idx][sum1] = min(difference_1, difference_2)
        return memo[idx][sum1]
