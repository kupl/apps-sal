class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        l = [0] * (len(nums) + 1)
        for a, b in requests:
            l[a] += 1
            l[b + 1] -= 1
        return sum(m * a for m, a in zip(sorted(accumulate(l[:-1])), sorted(nums))) % (10**9 + 7)
