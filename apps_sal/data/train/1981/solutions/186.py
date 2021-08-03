class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        count = [0] * (n + 1)

        for r in requests:
            start, end = r
            count[start] += 1
            count[end + 1] -= 1

        for i in range(1, n):
            count[i] = count[i - 1] + count[i]

        nums.sort(reverse=True)
        count.sort(reverse=True)
        res = 0
        for num, c in zip(nums, count):
            if c == 0:
                break
            else:
                res += num * c
        return res % (10**9 + 7)
