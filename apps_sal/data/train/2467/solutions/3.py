class Solution:

    def specialArray(self, nums: List[int]) -> int:
        res = -1
        nums.sort()
        for i in range(0, len(nums)):
            temp = 0
            for j in range(0, len(nums)):
                if nums[j] >= i + 1 and nums[j] != 0:
                    temp += 1
            if i + 1 == temp:
                res = i + 1 if i + 1 > res else res
        return res
