class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        count = [0] * (len(nums) + 1)
        for (start, end) in requests:
            count[start] += 1
            count[end + 1] -= 1
        for i in range(1, len(nums) + 1):
            count[i] += count[i - 1]
        count.pop()
        res = 0
        for (n, times) in zip(sorted(nums), sorted(count)):
            res += n * times
        return res % (10 ** 9 + 7)
