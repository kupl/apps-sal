class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums) <= 2: return max(nums+[0])
        now, last = 0, 0

        for i in nums:
            last, now = now, max(now, last + i)

        return now
