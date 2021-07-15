class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, nums[-1] + 1):
            if i == len([n for n in nums if n >= i]):
                return i
        return -1
