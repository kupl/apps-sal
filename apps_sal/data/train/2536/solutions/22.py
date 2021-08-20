class Solution:

    def findLucky(self, arr: List[int]) -> int:
        nums = []
        for c in arr:
            if c == arr.count(c):
                nums.append(c)
        if len(nums) > 0:
            return max(nums)
        else:
            return -1
