class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        freq = [0] * (n + 1)
        
        for i, j in requests:
            freq[i] += 1
            freq[j+1] -= 1
            
        for i in range(1, n + 1):
            freq[i] += freq[i - 1]
        freq = freq[:-1]    
        freq.sort()
        nums.sort()
        result = 0
        for i in range(n):
            result += freq[i] * nums[i]
        return result % 1_000_000_007
