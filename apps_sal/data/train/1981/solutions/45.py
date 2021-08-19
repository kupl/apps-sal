class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        counter = [0] * n
        for (start, end) in requests:
            if start < n:
                counter[start] += 1
            if end < n - 1:
                counter[end + 1] -= 1
        occurences = sorted(list(accumulate(counter)))
        nums.sort()
        res = sum([n * o for (n, o) in zip(nums, occurences)])
        return res % MOD
