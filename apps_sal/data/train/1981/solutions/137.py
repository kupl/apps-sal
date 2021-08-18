class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        m = len(requests)
        d = [0] * len(nums)
        R = sorted(requests)
        q = []
        j = 0
        for i in range(n):
            while q and q[0] < i:
                heapq.heappop(q)
            while j < m and R[j][0] <= i:
                heapq.heappush(q, R[j][1])
                j += 1
            d[i] = len(q)

        d.sort()
        nums.sort()
        ret = 0
        for i, j in zip(nums, d):
            ret += i * j
        return ret % (10 ** 9 + 7)
