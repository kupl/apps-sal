class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        nums = sorted(nums)
        mod = 10**9 + 7
        arry = [0] * (n + 1)
        for x, y in requests:
            arry[x] += 1
            arry[y + 1] -= 1
        for i in range(1, n + 1):
            arry[i] += arry[i - 1]
        q = []
        new_arry = [0] * n
        for idx, a in enumerate(arry):
            if a != 0:
                heapq.heappush(q, (-a, idx))
        while q:
            v, idx = heapq.heappop(q)
            if v == 0:
                break
            new_arry[idx] = nums.pop()
        ans = 0
        for v, times in zip(new_arry, arry):
            ans += v * times
        return ans % mod
