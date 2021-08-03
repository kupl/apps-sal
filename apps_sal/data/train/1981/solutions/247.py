class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        frequency = [0 for i in range(len(nums))]

        for u, v in requests:

            frequency[u] += 1
            if v + 1 < len(nums):
                frequency[v + 1] -= 1

        for i in range(1, len(frequency)):

            frequency[i] += frequency[i - 1]

        frequency.sort()
        nums.sort()

        Sum = 0
        while nums:

            Sum += nums.pop() * frequency.pop()

        return Sum % (10**9 + 7)
