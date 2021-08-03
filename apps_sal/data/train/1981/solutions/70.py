class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        counts = [0] * n

        for start, end in requests:
            counts[start] += 1
            if end < n - 1:
                counts[end + 1] -= 1

        cur_count = 0
        for i in range(n):
            cur_count += counts[i]
            counts[i] = cur_count

        nums.sort()
        counts.sort()
        res = 0
        for count, num in zip(counts, nums):
            res = (res + count * num) % mod

        return res
