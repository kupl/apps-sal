class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        N = len(nums)
        bucket = [0] * N
        for a, b in requests:
            if a < N:
                bucket[a] += 1
                if b < N - 1:
                    bucket[b + 1] -= 1
        bucket = list(itertools.accumulate(bucket))
        # for i in range(1, N):
        # bucket[i] = bucket[i-1] + bucket[i]
        nums.sort()
        bucket.sort()
        return sum(x * y for x, y in zip(nums, bucket)) % (10 ** 9 + 7)
