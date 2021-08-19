class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort()
        N = len(nums)
        bucket = [0] * N
        for (a, b) in requests:
            if a < N:
                bucket[a] += 1
            if b < N - 1:
                bucket[b + 1] -= 1
        for i in range(1, N):
            bucket[i] = bucket[i - 1] + bucket[i]
        bucket.sort()
        res = 0
        while bucket and bucket[-1] != 0:
            res = (res + bucket[-1] * nums[-1]) % (10 ** 9 + 7)
            bucket.pop()
            nums.pop()
        return res
