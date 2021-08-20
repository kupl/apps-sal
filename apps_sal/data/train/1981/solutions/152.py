class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        freq = [0] * n
        for (start, end) in requests:
            freq[start] += 1
            if end + 1 < n:
                freq[end + 1] -= 1
        cur = 0
        for i in range(len(freq)):
            cur += freq[i]
            freq[i] = cur
        freq.sort(reverse=True)
        nums.sort(reverse=True)
        return sum([freq[i] * nums[i] for i in range(n)]) % mod
