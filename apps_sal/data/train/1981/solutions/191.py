class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        N = len(nums)
        if N == 0:
            return 0
        index_freq = [0 for i in range(N + 1)]
        M = len(requests)
        for i in range(M):
            end = requests[i][1]
            start = requests[i][0]
            index_freq[start] += 1
            index_freq[end + 1] -= 1
        total_freq = [0 for i in range(N)]
        total_freq[0] = index_freq[0]
        for i in range(1, N):
            total_freq[i] = index_freq[i] + total_freq[i - 1]
        total_freq.sort(reverse=True)
        nums.sort(reverse=True)
        ret = 0
        for i in range(N):
            ret += nums[i] * total_freq[i]
        return ret % 1000000007
