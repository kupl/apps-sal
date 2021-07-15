class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse=True)
        ans = 0
        MOD = 10 ** 9 + 7
        cnt = [0] * (len(nums) + 1)
        for r in requests:
            cnt[r[0]] += 1
            cnt[r[-1] + 1] -= 1 
        for i in range(1, len(nums)):
            cnt[i] += cnt[i - 1]
        cnt = cnt[:-1]
        v = sorted(enumerate(cnt), key=operator.itemgetter(1), reverse=True)
        j = 0
        for _, k in v:
            ans += nums[j] * k
            j += 1
        return ans % MOD
