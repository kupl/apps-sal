class Solution:

    def findNumbers(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in nums:
            if i >= 10 and i < 100 or (i >= 1000 and i < 10000) or (i >= 100000 and i < 1000000):
                ans += 1
        return ans
