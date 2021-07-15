class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        total = 0
        prefix = [0] * len(nums)
        
        for x, y in requests:
            prefix[x] += 1
            if y < len(prefix) - 1:
                prefix[y + 1] -= 1
                
        for i in range(len(prefix) - 1):
            prefix[i+1] += prefix[i]
        
        nums.sort(reverse=True)
        prefix.sort(reverse=True)
        for i in range(len(nums)):
            total += (nums[i] * prefix[i])
        total %= (10 ** 9 + 7)
        return total

