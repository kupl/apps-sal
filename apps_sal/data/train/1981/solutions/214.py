class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = (10**9 + 7)
        n = len(nums)
        ranks = [0] * (n + 1)
        for start, end in requests:
            ranks[start] += 1
            ranks[end + 1] -= 1
        for i in range(1, n + 1):
            ranks[i] += ranks[i - 1]
        ranks = ranks[:n]
        ranks.sort()
        nums.sort()
        ans = 0
        for i in range(len(ranks)):
            ans += ranks[i] * nums[i]
        return ans % MOD
