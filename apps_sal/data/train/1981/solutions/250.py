class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        ind = [0] * (n + 1)

        for i, j in requests:
            ind[i] += 1
            ind[j + 1] -= 1

        for i in range(1, n):
            ind[i] += ind[i - 1]

        ind = sorted(list(zip(ind, range(n))))
        nums = sorted(nums)

        res = 0
        while ind:
            x, y = ind.pop()
            if x == 0:
                return res % (10**9 + 7)
            res += x * nums.pop()

        return res % (10**9 + 7)
