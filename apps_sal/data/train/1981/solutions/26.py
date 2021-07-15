class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        cnt = [0] * n
        for st, ed in requests:
            cnt[ed] += 1
            if st > 0: cnt[st-1] -= 1
        for i in range(n-2, -1, -1):
            cnt[i] += cnt[i+1]
                
        cnt.sort(reverse=1)
        nums.sort(reverse=1)
        ans = 0
        for c, x in zip(cnt, nums):
            if c == 0: break
            ans += c * x
        return ans % MOD
