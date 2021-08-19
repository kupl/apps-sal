class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # dp = {0}
        # sumA = sum(stones)
        # for a in stones:
        #     dp |= {a + i for i in dp}
        # return min(abs(sumA - i - i) for i in dp)
        dp, sumA = {0}, sum(stones)
        for a in stones:
            dp = {a + x for x in dp} | {a - x for x in dp}
        return min(abs(x) for x in dp)
