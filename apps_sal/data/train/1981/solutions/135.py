class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        imos = [0] * (n + 1)
        for l, r in requests:
            imos[l] += 1
            imos[r + 1] -= 1
        for i in range(n):
            imos[i + 1] += imos[i]
        del imos[-1]

        ans = 0
        for i, v in zip(sorted(nums), sorted(imos)):
            ans += i * v
            ans %= 10 ** 9 + 7
        return ans
