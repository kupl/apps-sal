class Solution:
    def rob(self, nums: List[int]) -> int:
        now, last = 0, 0

        for i in nums:
            last, now = now, max(now, last + i)

        return now
