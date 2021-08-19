class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        N = len(nums)
        i_count = [0] * N
        for (start, end) in requests:
            i_count[start] += 1
            if end + 1 < N:
                i_count[end + 1] -= 1
        for i in range(1, N):
            i_count[i] += i_count[i - 1]
        return sum((a * b for (a, b) in zip(sorted(i_count), sorted(nums)))) % 1000000007
