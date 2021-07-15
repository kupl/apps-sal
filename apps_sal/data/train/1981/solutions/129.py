class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        counts = [0] * 100001
        for start, end in requests:
            counts[start] += 1
            counts[end + 1] -= 1
        for i in range(100001):
            counts[i] += counts[i-1]
        result, mod = 0, 10 ** 9 + 7
        for num, count in zip(sorted(nums, reverse=True), sorted(counts, reverse=True)):
            result = (result + num * count) % mod
        return result

