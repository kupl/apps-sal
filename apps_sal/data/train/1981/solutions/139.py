class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        count = [0 for _ in range(n)]
        h = []
        requests.sort(key=lambda x: x[0])
        requests.append([float('inf'), float('inf')])
        cur = 0
        for s, e in requests:
            while h and h[0] < s:
                for i in range(cur, h[0] + 1):
                    count[i] += len(h)
                cur = h[0] + 1
                heapq.heappop(h)
            if s != float('inf'):
                for i in range(cur, s):
                    count[i] += len(h)
                cur = s
                heapq.heappush(h, e)
        mod = 10**9 + 7
        return sum([c * v for c, v in zip(sorted(nums), sorted(count))]) % mod
