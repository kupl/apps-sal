class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(0, len(nums)+1):
            if sum([n >= i for n in nums]) == i:
                return i
        return -1
