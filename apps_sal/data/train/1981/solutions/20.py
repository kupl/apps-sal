class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        N = len(nums)
        i_count = [0] * N

        for start, end in requests:
            i_count[start] += 1

            if end + 1 < N:
                i_count[end + 1] -= 1

        for i in range(1, N):
            i_count[i] += i_count[i - 1]

        s = 0
        m = 1000000007
        i_count.sort()
        nums.sort()
        for i in range(N):
            s += i_count[i] * nums[i]
            if s > m:
                s %= m

        return s
