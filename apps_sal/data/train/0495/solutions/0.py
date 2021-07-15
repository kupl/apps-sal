class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {0}
        total = sum(stones)
        for stone in stones:
            dp |= {_sum + stone for _sum in dp}
        return min(abs(total - _sum - _sum) for _sum in dp)
