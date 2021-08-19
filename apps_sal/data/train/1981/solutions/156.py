class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        f = [0 for i in range(len(nums) + 1)]
        for (i, j) in requests:
            f[i] += 1
            f[j + 1] -= 1
        pf = [f[0]]
        for i in range(1, len(f)):
            pf.append(pf[i - 1] + f[i])
        pf.sort(reverse=True)
        nums.sort(reverse=True)
        s = 0
        for i in range(len(nums)):
            s += pf[i] * nums[i]
        return s % (10 ** 9 + 7)
