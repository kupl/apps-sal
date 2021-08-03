from bisect import bisect_left


class Solution:
    def specialArray(self, nums: List[int]) -> int:

        nums.sort()
        l = len(nums)
        maxi = nums[-1]

        for i in range(maxi + 1):
            if l - bisect_left(nums, i) == i:
                return i

        return -1
