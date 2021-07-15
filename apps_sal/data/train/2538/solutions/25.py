class Solution:
    def countLargestGroup(self, n: int) -> int:
        nums = collections.defaultdict(int)
        maxFreq = 1
        maxCount = 0
        for i in range(1, n + 1):
            total = sum(list([int(x) for x in str(i)]))
            nums[total] = 1 + nums.get(total, 0)
            if nums[total] > maxFreq:
                maxFreq = nums[total]
                maxCount = 1
            elif nums[total] == maxFreq:
                maxCount += 1
        return maxCount

