class Solution:

    def countLargestGroup(self, n: int) -> int:
        nums = {}
        for i in range(1, n + 1):
            total = sum(list([int(x) for x in str(i)]))
            nums[total] = 1 + nums.get(total, 0)
        maxCount = max(nums.values())
        return list(nums.values()).count(maxCount)
