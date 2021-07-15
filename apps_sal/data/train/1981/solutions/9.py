class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        ans = [0]*(n+1)
        for i,j in requests:
            ans[i] += 1
            ans[j+1] -= 1
        for i in range(1,n):
            ans[i] += ans[i-1]
        ans.pop()
        result = 0
        for count, value in zip(sorted(ans),sorted(nums)):
            result += count*value
        return result % (10**9+7)
        

