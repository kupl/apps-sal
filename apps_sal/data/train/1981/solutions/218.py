class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        # We want to calculate the frequency for A[i].
        # Assign the big element A[i] to the position queried more frequently.
        n = len(nums)
        count = [0] * (n + 1)
        
        for i, j in requests:
            count[i] += 1
            count[j + 1] -= 1
            
        for i in range(1, n + 1):
            count[i] += count[i - 1]
            
        res = 0
        for v, c in zip(sorted(count[:-1]), sorted(nums)):
            res += v * c
            
        return res % (10**9 + 7)
    
    

