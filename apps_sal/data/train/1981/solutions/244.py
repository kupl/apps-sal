from heapq import heappush, heappop


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        count = [0] * (n + 1)
        for request in requests:
            start, end = request
            count[start] += 1
            count[end + 1] -= 1

        for i in range(1, n + 1):
            count[i] += count[i - 1]
        answer = 0
        nums.sort()
        c = count[:-1]
        c.sort()
        for a, b in zip(nums, c):
            answer += a * b

        mod = (10**9) + 7
        return answer % mod
