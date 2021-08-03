class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {0}
        sum_stones = sum(stones)

        for stone in stones:
            dp |= {stone + i for i in dp}

        return min(abs(sum_stones - i - i) for i in dp)
