class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        cnt = [0] * n
        for l, r in requests:
            cnt[l] += 1
            if r + 1 < n:
                cnt[r + 1] -= 1
        
        partial_sum = 0
        for i in range(n):
            cnt[i] += partial_sum
            partial_sum = cnt[i]
        
        nums.sort()
        cnt.sort()
        
        ans = 0
        for i in range(n):
            ans = (ans + nums[i] * cnt[i]) % int(1e9 + 7)
        return ans
            

