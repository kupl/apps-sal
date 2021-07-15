class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        counts = [0 for _ in range(n)]
        for i, j in requests:
            counts[i] += 1
            if j + 1 < n:
                counts[j+1] -= 1
        
        for i in range(1, n):
            counts[i] += counts[i-1]
        
        nums.sort()
        counts.sort()
        
        mod = 10 ** 9 + 7
        r = 0
        
        for i in range(n):
            r += nums[i] * counts[i]
        
        return r % mod
