class Solution:

    def specialArray(self, nums: List[int]) -> int:
        for i in range(min(len(nums), max(nums)) + 1):
            if i == len([x for x in nums if x >= i]):
                return i
        return -1
