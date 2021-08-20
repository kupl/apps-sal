class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        if nums == [] or requests == []:
            return 0
        l = len(nums)
        freqs = [0] * (l + 1)
        for request in requests:
            (start, end) = request
            freqs[start] += 1
            freqs[end + 1] -= 1
        for i in range(1, l + 1):
            freqs[i] += freqs[i - 1]
        nums = sorted(nums)
        freqs = sorted(freqs[:-1])
        ans = 0
        for i in range(l):
            if freqs[i] == 0:
                continue
            ans += freqs[i] * nums[i]
        return ans % (10 ** 9 + 7)
