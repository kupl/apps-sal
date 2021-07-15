class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        frequencies = [0] * len(nums)
        
        for start, end in requests:
            frequencies[start] += 1
            if end+1 < len(frequencies): frequencies[end + 1] -= 1

        for i in range(1, len(frequencies)):
            frequencies[i] = frequencies[i] + frequencies[i - 1]
        
        nums.sort(reverse=True)
        frequencies.sort(reverse=True)
        
        maxSum = 0
        for i in range(len(nums)):
            maxSum += nums[i] * frequencies[i]
            
        return maxSum % (10**9 + 7)
    
    
    
\"\"\"
def maxSumRangeQuery(self, A, req):
        n = len(A)
        count = [0] * (n + 1)
        for i, j in req:
            count[i] += 1
            count[j + 1] -= 1
        for i in xrange(1, n + 1):
            count[i] += count[i - 1]
        res = 0
        for v, c in zip(sorted(count[:-1]), sorted(A)):
            res += v * c
        return res % (10**9 + 7)
\"\"\"
