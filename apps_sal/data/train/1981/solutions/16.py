class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        l = len(nums)
        if l == 0: return 0
        acc = [0] * (l + 1)
        for r in requests:
            acc[r[0]] += 1
            acc[r[1] + 1] -= 1
        app = [0] * (l)
        app[0] = acc[0]
        for i in range(1, l):
            app[i] = app[i - 1] + acc[i]
        app.sort()
        nums.sort()
        return sum([app[i] * nums[i] for i in range(l)]) % (10 ** 9 + 7)
