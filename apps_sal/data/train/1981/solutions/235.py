class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        occurances = [0] * len(nums)
        for request in requests:
            occurances[request[0]] += 1
            if (request[1] + 1 < len(nums)):
                occurances[request[1] + 1] -= 1
        for i in range(1, len(nums)):
            occurances[i] += occurances[i - 1]
        mod = int(1e9 + 7)
        occurances.sort()
        nums.sort()
        res = 0
        for (x, y) in zip(occurances, nums):
            res = (res + x * y) % mod
        return res
