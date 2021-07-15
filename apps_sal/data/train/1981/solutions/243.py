class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        counts = [0] * (len(nums) + 1)
        for start, end in requests:
            counts[start] += 1
            counts[end + 1] -= 1
        for i in range(1, len(nums)):
            counts[i] += counts[i - 1]
        counts.sort(reverse = True)
        nums.sort(reverse = True)
        return sum(c * n for c, n in zip(counts, nums)) % (10 ** 9 + 7)

