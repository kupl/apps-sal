class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        M = 10**9+7
        
        n = len(nums)
        count = [0] * (n+1)
        for req in requests:
            count[req[0]] += 1
            count[req[1]+1] -= 1
            
        # print(count)
        for i in range(1, n+1):
            count[i] += count[i-1]
        # print(count)
        counts_ls = [(count[i], i) for i in range(n+1)]
        counts_ls.sort(key = lambda x: (-x[0], x[1]))
        # print(counts_ls)
        nums.sort(key = lambda x: -x)
        # print(nums)
        
        res = 0
        for i in range(n):
            res += nums[i] * counts_ls[i][0]
        return res % M
