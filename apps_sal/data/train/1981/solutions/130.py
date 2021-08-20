class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        c = [0] * n
        a = [0] * n
        b = [0] * n
        for x in requests:
            a[x[0]] += 1
            b[x[1]] += 1
        now = 0
        for i in range(n):
            now += a[i]
            c[i] = now
            now -= b[i]
        c.sort()
        nums.sort()
        ret = 0
        for i in range(n):
            ret += c[i] * nums[i]
        ret %= 10 ** 9 + 7
        return ret
