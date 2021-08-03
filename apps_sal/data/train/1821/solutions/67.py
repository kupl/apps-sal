import math


class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 64:
            return sorted(nums)
        if len(nums) <= 1:
            return nums
        c = 0
        maxN = nums[-1]
        al, ar = [], []

        for num in nums:
            if num < maxN:
                al.append(num)
            elif num > maxN:
                ar.append(num)
            elif num == maxN:
                c += 1

        return self.sortArray(al) + [maxN] * c + self.sortArray(ar)
