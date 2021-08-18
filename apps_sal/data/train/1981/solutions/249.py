class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse=True)
        N, M = len(nums), len(requests)
        freq = [0 for i in range(N + 1)]
        res = 0

        for start, end in requests:
            freq[start] += 1
            freq[end + 1] -= 1
        for i in range(1, N + 1):
            freq[i] += freq[i - 1]
        freq.sort(reverse=True)
        for i in range(N):
            res += freq[i] * nums[i]
            if freq[i] == 0 or nums[1] == 0:
                break
        return res % (10**9 + 7)
