class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        freqs = [0] * (len(nums) + 1)
        for s, e in requests:
            freqs[s] += 1
            freqs[e + 1] -= 1
        freqs.pop()
        f = 0
        for i, x in enumerate(freqs):
            f += x
            freqs[i] = f
        nums.sort()
        freqs.sort()
        result = 0
        for n, f in zip(nums, freqs):
            result += f * n
        return result % 1000000007

