
class Solution:
    def maxSumRangeQuery(self, nums: List[int], query: List[List[int]]) -> int:
        nums = sorted(nums)
        n = len(nums)
        freq = [0] * (n+1)
        for l, r in query:
            freq[l] += 1
            freq[r+1] -= 1
        for i in range(1, n):
            freq[i] += freq[i-1]
        freq = sorted(freq[:n])
        return sum(freq[i] * nums[i] for i in range(n)) % 1000000007
