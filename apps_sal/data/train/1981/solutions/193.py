class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        ans = 0
        
        freq = [0] * (n+1)
        for (a,b) in requests:
            freq[a] += 1
            freq[b + 1] -= 1
        for i in range(1,len(freq)):
            freq[i] += freq[i-1]
        freq.sort(reverse = True)
        nums.sort(reverse = True)
        return sum([freq[i]*nums[i] for i in range(n)])%MOD

